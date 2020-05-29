from psycopg2.extras import RealDictCursor
from designsQt import showMenu, addMenuShow, editShow, deleteShow, searchShowMenu, findShow, tableShow
import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QDialog
from PyQt5.QtCore import pyqtSlot
import UI
class ShowMenu(QMainWindow, showMenu.Ui_MainWindow):
    def __init__(self, connection):
        super().__init__()
        self.setupUi(self)
        self.connection = connection
        self.addShowBtn.clicked.connect(self.addShow)
        self.editShowBtn.clicked.connect(self.editShow)
        self.delShowBtn.clicked.connect(self.deleteShow)
        self.showShowBtn.clicked.connect(self.showShow)
        self.backBtn.clicked.connect(self.backShow)
        self.searchShowBtn.clicked.connect(self.searchShow)
        self.truncateShowBtn.clicked.connect(self.truncateShow)
        self.show()

    @pyqtSlot()
    def addShow(self):
        self.addShowWindow = AddShow(connection= self.connection)
        self.hide()
        self.addShowWindow.show()

    @pyqtSlot()
    def editShow(self):
        self.editShowWindow = EditShow(connection=self.connection)
        self.hide()
        self.editShowWindow.show()

    @pyqtSlot()
    def deleteShow(self):
        self.deleteShowWindow = DeleteShow(connection=self.connection)
        self.hide()
        self.deleteShowWindow.show()

    @pyqtSlot()
    def searchShow(self):
        self.searchShowWindow = SearchShow(connection=self.connection)
        self.hide()
        self.searchShowWindow.show()

    @pyqtSlot()
    def showShow(self):
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("select get_all_shows();")
        results = json.loads(json.dumps((cursor.fetchall())))
        if results[0]['get_all_shows']:
            self.hide()
            self.partSearchTb = SearchTable(connection=self.connection, list=results[0]['get_all_shows'])
            self.partSearchTb.show()
        else:
            self.errorLabel.setText('Table is empty')


    @pyqtSlot()
    def truncateShow(self):
        cursor = self.connection.cursor()
        cursor.execute("select truncate_actors();")
        cursor.execute("select truncate_shows();")
        cursor.close()
        print("Truncated")
        self.mainWindow = ShowMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()

    @pyqtSlot()
    def backShow(self):
        self.tableMenu = UI.TableMenu(connection = self.connection)
        self.hide()
        self.tableMenu.show()

class AddShow(QMainWindow, addMenuShow.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.connection = connection
        self.checkBtn.clicked.connect(self.addToDB)
        self.backBtn.clicked.connect(self.backToMain)
        self.show()

    @pyqtSlot()
    def backToMain(self):
        self.mainWindow = ShowMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()

    @pyqtSlot()
    def addToDB(self):
        name = self.textboxName.text()
        country = self.textboxCountry.text()
        seasons = self.spinBoxSeasons.value()
        episodes = self.spinBoxEpisodes.value()
        watched = self.spinBoxWatched.value()
        if name and country and seasons and episodes and watched:
            cursor = self.connection.cursor()
            try:
                cursor.execute(f"select add_show('{name}','{country}',{seasons}, {episodes}, {watched});")
                cursor.close()
                self.errorLabel.setText("Data were added successfully")
                self.mainWindow = ShowMenu(connection=self.connection)
                self.hide()
                self.mainWindow.show()
            except psycopg2.Error as e:
                self.errorLabel.setText(f"The error '{e}' was occurred")
        else:
            self.errorLabel.setText("You need to fill up all the gaps")

class EditShow(QMainWindow, editShow.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.connection = connection
        self.checkBtn.clicked.connect(self.editDB)
        self.backBtn.clicked.connect(self.backToMain)
        self.show()

    @pyqtSlot()
    def backToMain(self):
        self.mainWindow = ShowMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()

    @pyqtSlot()
    def editDB(self):
        id = self.idLine.text()
        if id:
            cursor = self.connection.cursor()
            cursor.execute(f"select check_show('{id}');")
            result = cursor.fetchall()
            if result != [(None,)]:
                name = self.textboxName.text()
                country = self.textboxCountry.text()
                seasons = self.spinBoxSeasons.value()
                episodes = self.spinBoxEpisodes.value()
                watched = self.spinBoxWatched.value()
                fl = 0
                fl_m = 0
                if name:
                    fl = 1
                    try:
                        cursor.execute(f"select update_show_name('{id}','{name}');")
                    except psycopg2.Error as e:
                        fl_m = 1
                        self.errorLabel.setText(f"The error '{e}' was occurred")
                if country and fl_m == 0:
                    fl = 1
                    try:
                        cursor.execute(f"select update_show_country('{id}','{country}');")
                    except psycopg2.Error as e:
                        fl_m = 1
                        self.errorLabel.setText(f"The error '{e}' was occurred")
                if seasons and fl_m == 0:
                    fl = 1
                    try:
                        cursor.execute(f"select update_show_seasons('{id}','{seasons}');")
                    except psycopg2.Error as e:
                        fl_m = 1
                        self.errorLabel.setText(f"The error '{e}' was occurred")
                if episodes and fl_m == 0:
                    fl = 1
                    try:
                        cursor.execute(f"select update_show_edisodes('{id}','{episodes}');")
                    except psycopg2.Error as e:
                        fl_m = 1
                        self.errorLabel.setText(f"The error '{e}' was occurred")
                if watched and fl_m == 0:
                    fl = 1
                    try:
                        cursor.execute(f"select update_show_watched('{id}','{watched}');")
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
        self.mainWindow = ShowMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()

class SearchShow(QMainWindow, searchShowMenu.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.connection = connection
        self.backBtn.clicked.connect(self.backToMain)
        self.byNameBtn.clicked.connect(self.searchByName)
        self.byCountryBtn.clicked.connect(self.searchByCountry)
        self.fullBtn.clicked.connect(self.fullData)
        self.show()

    @pyqtSlot()
    def searchByName(self):
        self.findMenu = FindShowBy(connection=self.connection, parametr='name')
        self.hide()
        self.findMenu.show()

    @pyqtSlot()
    def searchByCountry(self):
        self.hide()
        self.findMenu = FindShowBy(connection=self.connection, parametr='country')
        self.findMenu.show()

    @pyqtSlot()
    def fullData(self):
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("select get_all_shows();")
        results = json.loads(json.dumps((cursor.fetchall())))
        if results[0]['get_all_shows']:
            self.hide()
            self.partSearchTb = SearchTable(connection=self.connection, list=results[0]['get_all_shows'])
            self.partSearchTb.show()
        else:
            self.errorLabel.setText('Table is empty')

    @pyqtSlot()
    def backToMain(self):
        self.mainWindow = ShowMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()

class FindShowBy(QMainWindow, findShow.Ui_MainWindow):
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
        self.searchShow = SearchShow(connection=self.connection)
        self.hide()
        self.searchShow.show()

    @pyqtSlot()
    def Search(self):
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        if self.lineEdit.text():
            try:
                cursor.execute(f"select get_shows_by_{self.parametr}('{self.lineEdit.text()}');")
                results = json.loads(json.dumps((cursor.fetchall())))
                if results[0][f'get_shows_by_{self.parametr}']:
                    self.hide()
                    self.partSearchTb = SearchTable(connection=self.connection,
                                                        list=results[0][f'get_shows_by_{self.parametr}'])
                    self.partSearchTb.show()
                else:
                    self.errorLabel.setText(f'There is no info with {self.parametr}={self.lineEdit.text()}')
            except psycopg2.Error as e:
                self.errorLabel.setText(f"The error '{e}' was occurred")
        else:
            self.errorLabel.setText('You need to write info to find')


class SearchTable(QMainWindow, tableShow.Ui_MainWindow):
    def __init__(self, connection, list):
        super().__init__()
        self.setupUi(self, list=list)
        self.connection = connection
        self.backBtn.clicked.connect(self.backToSearchMenu)
        self.show()

    @pyqtSlot()
    def backToSearchMenu(self):
        self.searchShow = SearchShow(connection=self.connection)
        self.hide()
        self.searchShow.show()

class DeleteShow(QMainWindow, deleteShow.Ui_MainWindow):
    def __init__(self,connection):
        super().__init__()
        self.setupUi(self)
        self.connection = connection
        self.checkBtn.clicked.connect(self.deleteShow)
        self.backBtn.clicked.connect(self.backToMain)
        self.show()

    @pyqtSlot()
    def backToMain(self):
        self.mainWindow = ShowMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()

    @pyqtSlot()
    def deleteShow(self):
        id = self.idLine.text()
        if id:
            cursor = self.connection.cursor()
            try:
                cursor.execute(f"select check_show('{id}');")
                result = cursor.fetchall()
                if result != [(None,)]:
                    cursor.execute(f"select delete_show('{id}');")
                    cursor.close()
                    self.errorLabel.setText(f"Data with id = {id} were dropped successfully")
                else:
                    self.errorLabel.setText(f"Data with id = {id} doesnt exists")
            except psycopg2.Error as e:
                self.errorLabel.setText(f"The error '{e}' was occurred")
        else:
            self.errorLabel.setText("You fill up the id line")
        self.mainWindow = ShowMenu(connection=self.connection)
        self.hide()
        self.mainWindow.show()

    
        