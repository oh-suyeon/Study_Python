import sys

from PyQt5 import uic
from PyQt5.Qt import QColor
from PyQt5.QtWidgets import *
from random import random


form_class = uic.loadUiType("myqt08.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.doGame)
        self.le_mine.returnPressed.connect(self.doGame)
    
    def doGame(self):
        mine = self.le_mine.text()
        com = ""
        result = ""
        
        rnd = random()
        if rnd <= 0.3 :
            com = "가위"
        elif rnd <= 0.6 : 
            com = "바위"
        else :
            com = "보"
        
        # 길어지더라도 사람이 한 눈에 알아볼 수 있게 짜는 게 좋다.
        # if mine == "가위" and com == "가위"
        #     result = "비김" --> 이런 식으로 9개 경우를 나열하기
        if com == mine :
            result = "비김"
        elif com == "가위" and mine =="보" or com == "바위" and mine =="가위" or com == "보" and mine =="바위" :
            result = "패배"
        else :
            result = "승리"
            
        self.le_com.setText(com)
        self.le_result.setText(result)
        
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()