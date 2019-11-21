import sqlite3, sys
import os
import fingerprint_recog

from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error
from loginGUI import *
from signup import Signup
from info import InfoTable
from capture import show_webcam
from recognize_face import check_person

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.login_btn.clicked.connect(self.login_user)
        self.ui.signup_btn.clicked.connect(self.open_signup)
        self.show()

    def login_user(self):
        self.ui.label_response.clear()
        sql_statement = "select email, password from users where email like '"+self.ui.email_login.text()+"' and password like '"+self.ui.password_login.text()+"';"
        sql_level = "select usrlevel from users where email like '"+self.ui.email_login.text()+"' and password like '"+self.ui.password_login.text()+"';"

        try:
            # start a connection with the database
            with sqlite3.connect("aps.db") as conn:
                # initialize a cursor to execute the database commands
                cur = conn.cursor()
                cur.execute(sql_statement)
                row = cur.fetchone()
                # check if any rows were returned after using the user login and password given to make an sql query
                if row is None:
                    self.ui.label_response.setText("Sorry, incorrect email or password ")
                else:
                    cur.execute(sql_level)
                    row_level = cur.fetchone()[0]
                    if row_level == 1:
                        self.ui.label_response.setText("                           You are welcome ")
                        self.open_info(row_level)
                    elif row_level == 2:
                        if fingerprint_recog.main(self.ui.email_login.text()):
                            self.ui.label_response.setText("                           You are welcome ")
                            self.open_info(row_level)
                        else:
                            self.ui.label_response.setText("             Your finger does not match with the user login")
                    else:
                        if fingerprint_recog.main(self.ui.email_login.text()):
                            self.ui.label_response.setText("                          Initializing Webcam...")
                            self.ui.label_response.setText("    Press SpaceBar once you appear on the video feed")
                            # start the webcam and takes a picture once the user presses spacebar
                            show_webcam()
                            # returns a name from the dataset who the person in the picture seems to be
                            validated_user = check_person()
                            if validated_user == self.ui.email_login.text():
                                self.ui.label_response.setText("                           You are welcome ")
                                if os.path.exists("user_image.png"):
                                    os.remove("user_image.png")
                                self.open_info(row_level)
                            else:
                                self.ui.label_response.setText("             Your face does not match with the user login")
                        else:
                            self.ui.label_response.setText("             Your finger does not match with the user login")

        except Error as e:
            self.ui.label_response.setText("Error trying to log in")

    def open_info(self, level):
        self.uiInfo = InfoTable(level)

    def open_signup(self):
        self.uiSign = Signup()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())