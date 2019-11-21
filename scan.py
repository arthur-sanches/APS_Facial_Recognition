import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
import fingerprint_recog

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.result = self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Scan Digital")
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        result = self.openFileNameDialog()
        return(result)
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            result = fileName.split("aps/")
            return(str(result[1]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    exit()
    sys.exit(app.exec_())

