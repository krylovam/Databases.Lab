# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(40, 477, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 60, 361, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ShowBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ShowBtn.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ShowBtn.setFont(font)
        self.ShowBtn.setMouseTracking(True)
        self.ShowBtn.setObjectName("ShowBtn")
        self.verticalLayout.addWidget(self.ShowBtn)
        self.ActorBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ActorBtn.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ActorBtn.setFont(font)
        self.ActorBtn.setMouseTracking(True)
        self.ActorBtn.setObjectName("ActorBtn")
        self.verticalLayout.addWidget(self.ActorBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 21))
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
        self.ShowBtn.setText(_translate("MainWindow", "Таблица: NetflixShow"))
        self.ActorBtn.setText(_translate("MainWindow", "Таблица: Actors"))
        self.backBtn.setText(_translate("MainWindow", "Назад"))
