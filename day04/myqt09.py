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
        self.msg = QMessageBox()
        self.pb1.clicked.connect(lambda state, button=self.pb1 : self.numclick(state, button))
        self.pb2.clicked.connect(lambda state, button=self.pb2 : self.numclick(state, button))
        self.pb3.clicked.connect(lambda state, button=self.pb3 : self.numclick(state, button))
        self.pb4.clicked.connect(lambda state, button=self.pb4 : self.numclick(state, button))
        self.pb5.clicked.connect(lambda state, button=self.pb5 : self.numclick(state, button))
        self.pb6.clicked.connect(lambda state, button=self.pb6 : self.numclick(state, button))
        self.pb7.clicked.connect(lambda state, button=self.pb7 : self.numclick(state, button))
        self.pb8.clicked.connect(lambda state, button=self.pb8 : self.numclick(state, button))
        self.pb9.clicked.connect(lambda state, button=self.pb9 : self.numclick(state, button))
        self.pb0.clicked.connect(lambda state, button=self.pb0 : self.numclick(state, button))
        self.pb_call.clicked.connect(self.callclick)

    def numclick(self, state, button):
        print("self : ",self)
        print("self : ",self.sender().text())
        print("state : ",state)
        print("button : ",button)
        btn = button.text()
        
        text = self.le.text()
        text += btn
        
        self.le.setText(text)
        
    def callclick(self):
        text = self.le.text()
        self.le.setText("")
        
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('CALL')
        self.msg.setText('CALLING... \n' + text)
        self.msg.setStandardButtons(QMessageBox.Cancel)
        retval = self.msg.exec_()
        
        
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()