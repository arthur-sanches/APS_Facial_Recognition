import sqlite3, sys

from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error
from loginGUI import *
from signup import Signup


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.login_btn.clicked.connect(self.login_user)
        self.ui.signup_btn.clicked.connect(self.open_signup)
        self.show()

    def login_user(self):
        sql_statement = "select email, password from users where email like '"+self.ui.email_login.text()+"' and password like '"+self.ui.password_login.text()+"';"
        sql_level = "select usrlevel from users where email like '"+self.ui.email_login.text()+"' and password like '"+self.ui.password_login.text()+"';"

        try:
            with sqlite3.connect("aps/aps.db") as conn:
                cur = conn.cursor()
                cur.execute(sql_statement)
                row = cur.fetchone()
                if row is None:
                    self.ui.label_response.setText("Sorry, incorrect email or password ")
                else:
                    cur.execute(sql_level)
                    row_level = cur.fetchone()[0]
                    if row_level == 1:
                        self.ui.label_response.setText("          You are welcome ")
                    else:
                        self.ui.label_response.setText("Initiating webcam for facial recognition...")
        except Error as e:
            self.ui.label_response.setText("Error trying to log in")

    def face_reco(self):
        pass

    def open_signup(self):
        self.uiSign = Signup()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())