import sqlite3, sys

from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from infoGUI import *


class InfoTable(QDialog):

    def __init__(self, level=1):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.level = level
        self.ui.buttonTitle.clicked.connect(self.query_title)
        self.ui.buttonLevel.clicked.connect(self.query_level)
        self.ui.buttonDefaultQuery.clicked.connect(self.initial_query)
        self.initial_query()
        self.show()

    def initial_query(self):

        # clean the table to show new rows
        self.ui.tableWidget.clearContents()

        level = 1

        while level <= self.level:

            sql_statement = "SELECT * FROM info WHERE infolevel LIKE '"+str(level)+"';"

            try:
                # start a connection with the database
                with sqlite3.connect("aps.db") as conn:
                    # initialize a cursor to execute the database commands
                    cur = conn.cursor()
                    result = cur.execute(sql_statement)

                    for row_number, row_data, in enumerate(result):
                        self.ui.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    
            except Error as e:
                pass

            level += 1

    def query(self, statement):

        # clean the table to show new rows
        self.ui.tableWidget.clearContents()

        try:
            # start a connection with the database
            with sqlite3.connect("aps.db") as conn:
                # initialize a cursor to execute the database commands
                cur = conn.cursor()
                result = cur.execute(statement)

                for row_number, row_data, in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except Error as e:
            pass
                        
    def query_title(self):  

        if self.ui.lineEditTitle.text() == '':
            pass
        elif self.level == 3:
            sql_statement = "SELECT * FROM info WHERE title LIKE '%"+self.ui.lineEditTitle.text()+"%';"
            self.query(sql_statement)
        elif self.level == 2:
            sql_statement = "SELECT * FROM info WHERE title LIKE '%"+self.ui.lineEditTitle.text()+"%' AND (infolevel LIKE '2' OR '1');"
            self.query(sql_statement)
        else:
            sql_statement = "SELECT * FROM info WHERE title LIKE '%"+self.ui.lineEditTitle.text()+"%' AND infolevel LIKE '1';"
            self.query(sql_statement)

    def query_level(self):

        if self.ui.lineEditLevel.text() == '':
            pass
        elif int(self.ui.lineEditLevel.text()) > self.level:
            pass
        else:
            sql_statement = "SELECT * FROM info WHERE infolevel LIKE '"+self.ui.lineEditLevel.text()+"';"
            self.query(sql_statement)


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = InfoTable()
    w.show()
    sys.exit(app.exec_())