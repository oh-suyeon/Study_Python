import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from time import sleep
import threading
import socket 

form_class = uic.loadUiType("myqt_client.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        self.client_socket.connect(('192.168.42.149', 9999))
    
        self.pb.clicked.connect(self.send_message)
        self.le.returnPressed.connect(self.send_message)
        
        self.my_t1 = threading.Thread(target=self.recv_thread)
        self.my_t1.start()

    def send_message(self):        
        message = self.le.text()
        txt = "{}:{}".format(self.client_socket.getsockname()[0], message)
        self.client_socket.send(txt.encode())
        self.le.setText("")

    def recv_thread(self):
        while True: 
            data = self.client_socket.recv(1024) 
            str_new = repr(data.decode()) 
            self.te.append(str_new.replace("'", ""))
            self.te.moveCursor(QtGui.QTextCursor.End)
        
    def __del__(self):
        self.client_socket.close() 
            
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()