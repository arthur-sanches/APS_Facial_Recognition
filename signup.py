import sqlite3, sys

from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from signupGUI import *


class Signup(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.create_acc_btn.clicked.connect(self.insert_rows)
        self.show()

    def clear_fields(self):
        """Clear the information fields on the Signup page."""
        self.ui.name_signup.clear()
        self.ui.email_signup.clear()
        self.ui.password_signup.clear()
        self.ui.password_con_signup.clear()

        # checks a determined radio button then changes its properties in 
        # order to uncheck it without checking another radio button
        self.ui.lvl1_signup.setChecked(True)
        self.ui.lvl1_signup.setAutoExclusive(False)
        self.ui.lvl1_signup.setChecked(False)
        self.ui.lvl1_signup.setAutoExclusive(True)

    def insert_rows(self):
        self.ui.label_response.clear()
        """Insert new users' information into the database."""
        level = 0
        if self.ui.lvl3_signup.isChecked() == True:
            level = 3
        elif self.ui.lvl2_signup.isChecked() == True:
            level = 2
        else:
            level = 1

        if self.ui.password_signup.text() != self.ui.password_con_signup.text():
            self.ui.label_response.setText('Passwords are different')
        else:
            sql_statement="INSERT INTO users (name, email, password, usrlevel) VALUES ('" + self.ui.name_signup.text() + "','" + self.ui.email_signup.text() + "','" + self.ui.password_signup.text() + "','" + str(level) + "')"

            try:
                # start a connection with the database
                with sqlite3.connect("aps.db") as conn:
                    # initialize a cursor to execute the database commands
                    cur = conn.cursor()
                    cur.execute(sql_statement)
                    self.ui.label_response.setText("User account created")
                    self.clear_fields()
            except Error as e:
                self.ui.label_response.setText("Error creating account")

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Signup()
    w.show()
    sys.exit(app.exec_())