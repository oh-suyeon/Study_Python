import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui

form_class = uic.loadUiType("myomok01.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.idx = 0
        self.setupUI(self)
        self.pb1.clicked.connect(self.myclick)
    
        pb2 = QPushButton(self)
        pb2.setText('Button&2')
    
    def myclick(self):
        self.idx += 1 
        print(self.idx)
        namuji = self.idx % 3
        self.pb1.setIcon(QtGui.QIcon('images/{}.png'.format(namuji)))
        
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()