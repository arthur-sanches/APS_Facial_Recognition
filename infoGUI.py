# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(802, 513)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 160, 801, 351))
        self.tableWidget.setMinimumSize(QtCore.QSize(801, 0))
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(189)
        self.buttonTitle = QtWidgets.QPushButton(Dialog)
        self.buttonTitle.setGeometry(QtCore.QRect(120, 90, 131, 27))
        self.buttonTitle.setObjectName("buttonTitle")
        self.buttonLevel = QtWidgets.QPushButton(Dialog)
        self.buttonLevel.setGeometry(QtCore.QRect(530, 90, 131, 27))
        self.buttonLevel.setObjectName("buttonLevel")
        self.lineEditTitle = QtWidgets.QLineEdit(Dialog)
        self.lineEditTitle.setGeometry(QtCore.QRect(60, 30, 251, 27))
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.lineEditLevel = QtWidgets.QLineEdit(Dialog)
        self.lineEditLevel.setGeometry(QtCore.QRect(470, 30, 251, 27))
        self.lineEditLevel.setObjectName("lineEditLevel")
        self.buttonDefaultQuery = QtWidgets.QPushButton(Dialog)
        self.buttonDefaultQuery.setGeometry(QtCore.QRect(328, 90, 131, 27))
        self.buttonDefaultQuery.setObjectName("buttonDefaultQuery")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Information Table"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "CSV Link"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "PDF Link"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Info Level"))
        self.buttonTitle.setText(_translate("Dialog", "Filter by Title"))
        self.buttonLevel.setText(_translate("Dialog", "Filter by Level"))
        self.buttonDefaultQuery.setText(_translate("Dialog", "Show Everything"))

