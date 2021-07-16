import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from time import sleep
import threading

form_class = uic.loadUiType("myqt_messenger_th_o.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    
    # 쓰레드를 호출한다.
    def myclick(self):
        my_t1 = threading.Thread(target=self.myfunc_th)
        my_t1.start()
        # for i in range(5) :
        #     sleep(1)
        #     a = self.lbl.text()
        #     int_a = int(a)
        #     int_a += 1
        #     self.lbl.setText(str(int_a))

    # 쓰레드로 돌릴 함수.
    # 이 함수를 직접 돌리면 sleep 때문에 gui가 먹통이 되는 문제가 생긴다. 
    def myfunc_th(self):
        for i in range(5) :
            sleep(1)
            a = self.lbl.text()
            int_a = int(a)
            int_a += 1
            self.lbl.setText(str(int_a))
            
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()