# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editActor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(20, 477, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.checkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.checkBtn.setGeometry(QtCore.QRect(670, 480, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBtn.setFont(font)
        self.checkBtn.setObjectName("checkBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.idLine = QtWidgets.QLineEdit(self.centralwidget)
        self.idLine.setGeometry(QtCore.QRect(50, 90, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idLine.setFont(font)
        self.idLine.setText("")
        self.idLine.setObjectName("idLine")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(160, 370, 431, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.errorLabel.setFont(font)
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 190, 491, 461))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.labelName = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.textboxName = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textboxName.setFont(font)
        self.textboxName.setObjectName("textboxName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textboxName)
        self.labelCharacterName = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelCharacterName.setFont(font)
        self.labelCharacterName.setObjectName("labelCharacterName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelCharacterName)
        self.textboxCharacterName = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textboxCharacterName.setFont(font)
        self.textboxCharacterName.setObjectName("textboxCharacterName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textboxCharacterName)
        self.labelShowId = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelShowId.setFont(font)
        self.labelShowId.setObjectName("labelShowId")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelShowId)
        self.spinBoxShowId = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBoxShowId.setObjectName("spinBoxShowId")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxShowId)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.checkBtn.setText(_translate("MainWindow", "Готово"))
        self.label.setText(_translate("MainWindow", "Введите id поля, которое хотите изменить"))
        self.label_2.setText(_translate("MainWindow", "Введите значения для изменения"))
        self.labelName.setText(_translate("MainWindow", "Имя:"))
        self.labelCharacterName.setText(_translate("MainWindow", "Имя персонажа:"))
        self.labelShowId.setText(_translate("MainWindow", "id show"))
