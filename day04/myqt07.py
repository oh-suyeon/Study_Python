import sys

from PyQt5 import uic
from PyQt5.Qt import QColor
from PyQt5.QtWidgets import *
from random import random


form_class = uic.loadUiType("myqt07.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick)
    
    def myclick(self):
        mine = self.le_mine.text()
        com = ""
        result = ""
        
        rnd = random()
        if rnd < 0.5 :
            com = "홀"
        else : 
            com = "짝"
        
        if com == mine :
            result = "승리"
        else :
            result = "패배"
        
        self.le_com.setText(com)
        self.le_result.setText(result)
        
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()