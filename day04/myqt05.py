import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("myqt06.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    
    def myclick(self):
        dan = int(self.le.text())
        
        print(dan)
        
        gugudan = dan + "x" + 1 + "=" + (dan * 1) + "\n"
        gugudan += dan + "x" + 2 + "=" + (dan * 2) + "\n"
        gugudan += dan + "x" + 3 + "=" + (dan * 3) + "\n"
        gugudan += dan + "x" + 4 + "=" + (dan * 4) + "\n"
        gugudan += dan + "x" + 5 + "=" + (dan * 5) + "\n"
        gugudan += dan + "x" + 6 + "=" + (dan * 6) + "\n"
        gugudan += dan + "x" + 7 + "=" + (dan * 7) + "\n"
        gugudan += dan + "x" + 8 + "=" + (dan * 8) + "\n"
        gugudan += dan + "x" + 9 + "=" + (dan * 9) + "\n"
        
        self.te.setText(gugudan)
        
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()