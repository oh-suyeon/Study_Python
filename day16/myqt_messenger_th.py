import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from time import sleep

form_class = uic.loadUiType("myqt_messenger_th.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le.returnPressed.connect(self.myclick)

        for i in range(5) :
            sleep(1)
            self.myclick2(str(i))
        

    def myclick2(self,a): #이벤트로 호출되는 게 아니라 들어오는 글자를 넣어줌
        print(a)

    def myclick(self):
        str_new = self.le.text()
        str_old = self.te.toPlainText()
        txt = str_old + "\n" + str_new
        self.te.setPlainText(txt)
        self.le.setText("")
        self.te.moveCursor(QtGui.QTextCursor.End)
        
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()