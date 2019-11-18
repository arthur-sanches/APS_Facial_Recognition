# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signupGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(497, 339)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 81, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 131, 17))
        self.label_4.setObjectName("label_4")
        self.lvl1_signup = QtWidgets.QRadioButton(Dialog)
        self.lvl1_signup.setGeometry(QtCore.QRect(70, 220, 117, 21))
        self.lvl1_signup.setObjectName("lvl1_signup")
        self.lvl2_signup = QtWidgets.QRadioButton(Dialog)
        self.lvl2_signup.setGeometry(QtCore.QRect(70, 250, 117, 22))
        self.lvl2_signup.setObjectName("lvl2_signup")
        self.lvl3_signup = QtWidgets.QRadioButton(Dialog)
        self.lvl3_signup.setGeometry(QtCore.QRect(70, 280, 117, 22))
        self.lvl3_signup.setObjectName("lvl3_signup")
        self.create_acc_btn = QtWidgets.QPushButton(Dialog)
        self.create_acc_btn.setGeometry(QtCore.QRect(260, 280, 131, 27))
        self.create_acc_btn.setObjectName("create_acc_btn")
        self.name_signup = QtWidgets.QLineEdit(Dialog)
        self.name_signup.setGeometry(QtCore.QRect(160, 20, 281, 27))
        self.name_signup.setObjectName("name_signup")
        self.email_signup = QtWidgets.QLineEdit(Dialog)
        self.email_signup.setGeometry(QtCore.QRect(160, 70, 281, 27))
        self.email_signup.setObjectName("email_signup")
        self.password_signup = QtWidgets.QLineEdit(Dialog)
        self.password_signup.setGeometry(QtCore.QRect(160, 120, 281, 27))
        self.password_signup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_signup.setObjectName("password_signup")
        self.password_con_signup = QtWidgets.QLineEdit(Dialog)
        self.password_con_signup.setGeometry(QtCore.QRect(160, 170, 281, 27))
        self.password_con_signup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_con_signup.setObjectName("password_con_signup")
        self.label_response = QtWidgets.QLabel(Dialog)
        self.label_response.setGeometry(QtCore.QRect(246, 230, 211, 20))
        self.label_response.setText("")
        self.label_response.setObjectName("label_response")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name :"))
        self.label_2.setText(_translate("Dialog", "E-mail :"))
        self.label_3.setText(_translate("Dialog", "Password :"))
        self.label_4.setText(_translate("Dialog", "Confirm Password :"))
        self.lvl1_signup.setText(_translate("Dialog", "Level 1"))
        self.lvl2_signup.setText(_translate("Dialog", "Level 2"))
        self.lvl3_signup.setText(_translate("Dialog", "Level 3"))
        self.create_acc_btn.setText(_translate("Dialog", "Create Account"))

