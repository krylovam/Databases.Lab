# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchShowMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(20, 477, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(350, 450, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.errorLabel.setFont(font)
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 110, 391, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.byNameBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.byNameBtn.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.byNameBtn.setFont(font)
        self.byNameBtn.setObjectName("byNameBtn")
        self.verticalLayout.addWidget(self.byNameBtn)
        self.byCountryBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.byCountryBtn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.byCountryBtn.setFont(font)
        self.byCountryBtn.setObjectName("byCountryBtn")
        self.verticalLayout.addWidget(self.byCountryBtn)
        self.fullBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.fullBtn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arialk")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fullBtn.setFont(font)
        self.fullBtn.setObjectName("fullBtn")
        self.verticalLayout.addWidget(self.fullBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backBtn.setText(_translate("MainWindow", "Назад"))
        self.byNameBtn.setText(_translate("MainWindow", "Найти по названию"))
        self.byCountryBtn.setText(_translate("MainWindow", "Найти по стране"))
        self.fullBtn.setText(_translate("MainWindow", "Показать всю таблицу"))
