# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(496, 339)
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(190, 230, 99, 27))
        self.login_btn.setObjectName("login_btn")
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(190, 280, 101, 27))
        self.signup_btn.setObjectName("signup_btn")
        self.email_login = QtWidgets.QLineEdit(Dialog)
        self.email_login.setGeometry(QtCore.QRect(130, 60, 291, 27))
        self.email_login.setObjectName("email_login")
        self.password_login = QtWidgets.QLineEdit(Dialog)
        self.password_login.setGeometry(QtCore.QRect(130, 120, 291, 27))
        self.password_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_login.setObjectName("password_login")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 120, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 51, 17))
        self.label_2.setObjectName("label_2")
        self.label_response = QtWidgets.QLabel(Dialog)
        self.label_response.setGeometry(QtCore.QRect(70, 170, 351, 20))
        self.label_response.setText("")
        self.label_response.setObjectName("label_response")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.signup_btn.setText(_translate("Dialog", "Signup"))
        self.label.setText(_translate("Dialog", "Password :"))
        self.label_2.setText(_translate("Dialog", "E-mail :"))

