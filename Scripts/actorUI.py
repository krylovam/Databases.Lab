from psycopg2.extras import RealDictCursor
from designsQt import actorsMenu, addMenuActor, editActor, deleteActor, searchActorMenu, findActor, tableActor
import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QDialog
from PyQt5.QtCore import pyqtSlot
import UI
class ActorMenu(QMainWindow, actorsMenu.Ui_MainWindow):
    def __init__(self, connection):
        super().__init__()
        self.setupUi(self)
        self.connection = connection
        self.addActorBtn.clicked.connect(self.addActor)
        self.editActorBtn.clicked.connect(self.editActor)
        self.delActorBtn.clicked.connect(self.deleteActor)
        self.showActorBtn.clicked.connect(self.showActor)
        self.backBtn.clicked.connect(self.backActor)
        self.findActorBtn.clicked.connect(self.searchActor)
        self.truncateActorBtn.clicked.connect(self.truncateActor)
        self.show()

    @pyqtSlot()
    def addActor(self):
        self.addActorWindow = AddActor(connection=self.connection)
        self.hide()
        self.addActorWindow.show()

    @pyqtSlot()
    def editActor(self):
        self.editActorWindow = EditActor(connection=self.connection)
        self.hide()
        self.editActorWindow.show()

    @pyqtSlot()
    def deleteActor(self):
        self.deleteActorWindow = DeleteActor(connection=self.connection)
        self.hide()
        self.deleteActorWindow.show()

    @pyqtSlot()
    def searchActor(self):
        self.searchActorWindow = SearchActor(connection=self.connection)
        self.hide()
        self.searchActorWindow.show()

    @pyqtSlot()
    def showActor(self):
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("select get_all_actors();")
        results = json.loads(json.dumps((cursor.fetchall())))
        if results[0]['get_all_actors']:
            self.hide()
            self.partSearchTb = SearchTable(connection=self.connection, list=results[0]['get_all_actors'])
            self.partSearchTb.show()
        else:
            self.errorLabel.setText('Table is empty')

    @pyqtSlot()
    def truncateActor(self):
        cursor = self.connection.cursor()
        cursor.execute("select truncate_actors();")
        cursor.close()
        print("Truncated")
        self.mainWindow = ActorMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()


    @pyqtSlot()
    def backActor(self):
        self.tableMenu = UI.TableMenu(connection=self.connection)
        self.hide()
        self.tableMenu.show()
        
class AddActor(QMainWindow, addMenuActor.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.connection = connection
        self.checkBtn.clicked.connect(self.addToDB)
        self.backBtn.clicked.connect(self.backToMain)
        self.show()

    @pyqtSlot()
    def backToMain(self):
        self.mainWindow = ActorMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()

    @pyqtSlot()
    def addToDB(self):
        name = self.textboxName.text()
        characterName = self.textboxCharacterName.text()
        showId = self.spinBoxShowId.value()
        if name and characterName and showId:
            cursor = self.connection.cursor()
            try:
                cursor.execute(f"select add_actor('{name}',{showId}, '{characterName}');")
                cursor.close()
                self.errorLabel.setText("Data were added successfully")
                self.mainWindow = ActorMenu(connection=self.connection)
                self.hide()
                self.mainWindow.show()
            except psycopg2.Error as e:
                self.errorLabel.setText(f"The error '{e}' was occurred")
        else:
            self.errorLabel.setText("You need to fill up all the gaps")

class EditActor(QMainWindow, editActor.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.connection = connection
        self.checkBtn.clicked.connect(self.editDB)
        self.backBtn.clicked.connect(self.backToMain)
        self.show()

    @pyqtSlot()
    def backToMain(self):
        self.mainWindow = ActorMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()

    @pyqtSlot()
    def editDB(self):
        id = self.idLine.text()
        if id:
            cursor = self.connection.cursor()
            cursor.execute(f"select check_actor('{id}');")
            result = cursor.fetchall()
            if result != [(None,)]:
                name = self.textboxName.text()
                characterName = self.textboxCharacterName.text()
                showId = self.spinBoxShowId.value()
                fl = 0
                fl_m = 0
                if name:
                    fl = 1
                    try:
                        cursor.execute(f"select update_actor_name('{id}','{name}');")
                    except psycopg2.Error as e:
                        fl_m = 1
                        self.errorLabel.setText(f"The error '{e}' was occurred")
                if showId and fl_m == 0:
                    fl = 1
                    try:
                        cursor.execute(f"select update_actor_show('{id}','{showId}');")
                    except psycopg2.Error as e:
                        fl_m = 1
                        self.errorLabel.setText(f"The error '{e}' was occurred")
                if characterName and fl_m == 0:
                    fl = 1
                    try:
                        cursor.execute(f"select update_actor_charactername('{id}','{characterName}');")
                    except psycopg2.Error as e:
                        fl_m = 1
                        self.errorLabel.setText(f"The error '{e}' was occurred")
                if fl == 1 and fl_m == 0:
                    self.errorLabel.setText("Info was updated successfully")
                elif fl == 0:
                    self.errorLabel.setText("Fill up info for changing")
            else:
                self.errorLabel.setText(f"Data with id = {id} doesnt exists")
        else:
            self.errorLabel.setText("ID line is empty")
        self.mainWindow = ActorMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()

class SearchActor(QMainWindow, searchActorMenu.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.connection = connection
        self.backBtn.clicked.connect(self.backToMain)
        self.byNameBtn.clicked.connect(self.searchByName)
        self.byCharacterNameBtn.clicked.connect(self.searchByNameOfCharacter)
        self.byShowIdBtn.clicked.connect(self.searchByShowId)
        self.fullBtn.clicked.connect(self.fullData)
        self.show()

    @pyqtSlot()
    def searchByName(self):
        self.findMenu = FindActorBy(connection=self.connection, parametr='name')
        self.hide()
        self.findMenu.show()

    @pyqtSlot()
    def searchByNameOfCharacter(self):
        self.hide()
        self.findMenu = FindActorBy(connection=self.connection, parametr='charactername')
        self.findMenu.show()

    @pyqtSlot()
    def searchByShowId(self):
        self.hide()
        self.findMenu = FindActorBy(connection=self.connection, parametr='show')
        self.findMenu.show()

    @pyqtSlot()
    def fullData(self):
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("select get_all_actors();")
        results = json.loads(json.dumps((cursor.fetchall())))
        if results[0]['get_all_actors']:
            self.hide()
            self.partSearchTb = SearchTable(connection=self.connection, list=results[0]['get_all_actors'])
            self.partSearchTb.show()
        else:
            self.errorLabel.setText('Table is empty')

    @pyqtSlot()
    def backToMain(self):
        self.mainWindow = ActorMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()

class FindActorBy(QMainWindow, findActor.Ui_MainWindow):
    def __init__(self, connection, parametr):
        super().__init__()
        self.setupUi(self)
        self.parametr = parametr
        self.connection = connection
        self.mainLabel.setText(f"Input {self.parametr}")
        self.findBtn.clicked.connect(self.Search)
        self.backBtn.clicked.connect(self.backToSearchMenu)
        self.show()

    @pyqtSlot()
    def backToSearchMenu(self):
        self.searchActor = SearchActor(connection=self.connection)
        self.hide()
        self.searchActor.show()

    @pyqtSlot()
    def Search(self):
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        if self.lineEdit.text():
            try:
                cursor.execute(f"select get_actors_by_{self.parametr}('{self.lineEdit.text()}');")
                results = json.loads(json.dumps((cursor.fetchall())))
                if results[0][f'get_actors_by_{self.parametr}']:
                    self.hide()
                    self.partSearchTb = SearchTable(connection=self.connection,
                                                        list=results[0][f'get_actors_by_{self.parametr}'])
                    self.partSearchTb.show()
                else:
                    self.errorLabel.setText(f'There is no info with {self.parametr}={self.lineEdit.text()}')
            except psycopg2.Error as e:
                self.errorLabel.setText(f"The error '{e}' was occurred")
        else:
            self.errorLabel.setText('You need to write info to find')


class SearchTable(QMainWindow, tableActor.Ui_MainWindow):
    def __init__(self, connection, list):
        super().__init__()
        self.setupUi(self, list=list)
        self.connection = connection
        self.backBtn.clicked.connect(self.backToSearchMenu)
        self.show()

    @pyqtSlot()
    def backToSearchMenu(self):
        self.searchActor = SearchActor(connection=self.connection)
        self.hide()
        self.searchActor.show()

class DeleteActor(QMainWindow, deleteActor.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.connection = connection
        self.checkBtn.clicked.connect(self.deleteActor)
        self.backBtn.clicked.connect(self.backToMain)
        self.show()

    @pyqtSlot()
    def backToMain(self):
        self.mainWindow = ActorMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()

    @pyqtSlot()
    def deleteActor(self):
        id = self.idLine.text()
        if id:
            cursor = self.connection.cursor()
            try:
                cursor.execute(f"select check_actor('{id}');")
                result = cursor.fetchall()
                if result != [(None,)]:
                    cursor.execute(f"select delete_actor('{id}');")
                    cursor.close()
                    self.errorLabel.setText(f"Data with id = {id} were dropped successfully")
                else:
                    self.errorLabel.setText(f"Data with id = {id} doesnt exists")
            except psycopg2.Error as e:
                self.errorLabel.setText(f"The error '{e}' was occurred")
        else:
            self.errorLabel.setText("You fill up the id line")
        self.mainWindow = ActorMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()
