from random import random
import sys

from PyQt5 import uic
from PyQt5.Qt import QColor, QSize
from PyQt5.QtWidgets import *


form_class = uic.loadUiType("myqt09.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.numclick)
        self.pb2.clicked.connect(self.numclick)
        self.pb3.clicked.connect(self.numclick)
        self.pb4.clicked.connect(self.numclick)
        self.pb5.clicked.connect(self.numclick)
        self.pb6.clicked.connect(self.numclick)
        self.pb7.clicked.connect(self.numclick)
        self.pb8.clicked.connect(self.numclick)
        self.pb9.clicked.connect(self.numclick)
        self.pb0.clicked.connect(self.numclick)
        self.pb_call.clicked.connect(self.callclick)

    def numclick(self):
        #print("self : ",self)
        btn = self.sender().text()
        text = self.le.text()
        text += btn
        
        self.le.setText(text)
        
    def callclick(self):
        text = self.le.text()
        self.le.setText("")
        
        QMessageBox.information(self, 'CALL', 'CALLING... \n' + text)
        
        
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()