# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableShow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, list):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        gridLayout = QtWidgets.QGridLayout()
        self.centralwidget.setLayout(gridLayout)

        table = QtWidgets.QTableWidget(self)
        headers = ['id', 'name_show', 'country', 'numberofseasons', 'numberofepisodes', 'watched', 'rest']
        table.setColumnCount(len(headers))
        table.setRowCount(len(list))

        table.setHorizontalHeaderLabels(headers)

        for row in range(len(list)):
            for col in range(len(headers)):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(str(list[row][headers[col]])))
        table.resizeColumnsToContents()

        gridLayout.addWidget(table, 0, 0)
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(0, 610, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 21))
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
