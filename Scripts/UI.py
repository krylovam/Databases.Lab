import psycopg2
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QDialog
from PyQt5.QtCore import pyqtSlot
from scripts_sql import create_new_database, all_functions
from designsQt import firstMenu, mainMenu, tableMenu, errorDialog1, errorDialog2
import showUI
import actorUI
import activation
import json
import sys



class ErrorDialog1(QDialog, errorDialog1.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.BtnOnClick)
        self.show()

    @pyqtSlot()
    def BtnOnClick(self):
        #self.hide()
        window = FirstMenu()

class ErrorDialog2(QDialog, errorDialog2.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.BtnOnClick)
        self.show()

    @pyqtSlot()
    def BtnOnClick(self):
        self.hide()
        window = FirstMenu()

class  FirstMenu(QMainWindow, firstMenu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.newDBBtn.clicked.connect(self.newDBBtnOnClick)
        self.oldDBBtn.clicked.connect(self.oldDBBtnOnClick)
        self.DeleteDBBtn.clicked.connect(self.DeleteDBBtnOnClick)
        self.show()

    def create_db(self):
        try:
            connection_user = activation.userActivation()
            print("Read text")
            self.ErrorLabel.setText("Delete database before creation")
            return 1
        except:
            connection_root = activation.rootActivation()
            cursor = connection_root.cursor()
            cursor.execute(create_new_database)
            cursor.execute("select create_database();")
            cursor.close()
            connection_root.close()
            connection_user = activation.userActivation()
            activation.activate_functions(connection_user)
            try:
                cursor.execute(all_functions)
            except:
                print("Database has created successfully")
            return 0

    def open_db(self):
        try:
            connection_user = activation.userActivation()
            print("Database is open")
            return connection_user
        except:
            self.ErrorLabel.setText("This data base does not exist. You should create it firstly")
            return None

    @pyqtSlot()
    def newDBBtnOnClick(self):
        ans = self.create_db()
        if ans == 0 :
            self.hide()
            self.tableMenu = TableMenu(connection=user_connection)
            self.tableMenu.show()
        else:
            window = ErrorDialog1()
            window.show()


    @pyqtSlot()
    def oldDBBtnOnClick(self):
        user_connection  = self.open_db()
        if user_connection:
            self.hide()
            self.tableMenu = TableMenu(connection=user_connection)
            self.tableMenu.show()
        else:
            window = ErrorDialog1()
            window.show()
            #self.hide()

    @pyqtSlot()
    def DeleteDBBtnOnClick(self):
        root_connection = activation.rootActivation()
        cursor = root_connection.cursor()
        try:
            cursor.execute('select drop_database();')
            print("Database was dropped")
        except psycopg2.OperationalError as exep:
            print(exep)
        finally:
            cursor.close()
            root_connection.close()
        self.hide()
        self.__init__()

class TableMenu(QMainWindow, tableMenu.Ui_MainWindow):

    def __init__(self, connection):
        super().__init__()
        self.setupUi(self)
        self.connection = connection
        self.ShowBtn.clicked.connect(self.NetflixTable)
        self.ActorBtn.clicked.connect(self.ActorTable)
        self.backBtn.clicked.connect(self.backFirst)
        self.show()

    @pyqtSlot()
    def NetflixTable(self):
        self.mainMenu = showUI.ShowMenu(connection = self.connection)
        self.hide()
        self.mainMenu.show()

    @pyqtSlot()
    def ActorTable(self):
        self.mainMenu = actorUI.ActorMenu(connection = self.connection)
        self.hide()
        self.mainMenu.show()

    @pyqtSlot()
    def backFirst(self):
        self.firstMenu = FirstMenu()
        self.hide()
        self.firstMenu.show()

def main():
    connection = activation.rootActivation()
    cursor = connection.cursor()
    cursor.execute("SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity "
                   "WHERE pg_stat_activity.datname = 'labdb' AND pid <> pg_backend_pid();")
    cursor.close()
    connection.close()
    app = QApplication(sys.argv)
    window = FirstMenu()
    app.exec_()
if __name__ == '__main__':
    main()


