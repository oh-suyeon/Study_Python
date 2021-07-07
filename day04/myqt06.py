import sys

from PyQt5 import uic
from PyQt5.Qt import QColor
from PyQt5.QtWidgets import *


form_class = uic.loadUiType("myqt06.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    
    def myclick(self):
        dan = int(self.le.text())
        
        gugudan  = "{} * {} = {}\n".format(dan,1,dan*1)
        gugudan += "{} * {} = {}\n".format(dan,2,dan*2)
        gugudan += "{} * {} = {}\n".format(dan,3,dan*3)
        gugudan += "{} * {} = {}\n".format(dan,4,dan*4)
        gugudan += "{} * {} = {}\n".format(dan,5,dan*5)
        gugudan += "{} * {} = {}\n".format(dan,6,dan*6)
        gugudan += "{} * {} = {}\n".format(dan,7,dan*7)
        gugudan += "{} * {} = {}\n".format(dan,8,dan*8)
        gugudan += "{} * {} = {}\n".format(dan,9,dan*9)
        
        # for문 돌리기
        gugu = ""
        for i in range(1,9+1) :
            gugu += "{} * {} = {} \n".format(dan,i,dan*i)
        
        self.te.setText(gugu)
        
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()