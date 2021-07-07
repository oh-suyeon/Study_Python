import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.Qt import QSize
from networkx.generators import line
import numpy as np

form_class = uic.loadUiType("myomok02.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        
        # 칸의 상태 (0, 1, 2)
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
                        
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            ]        
        
        # 돌을 둘 차례를 정하는 인덱스 (turn_idx % 2 값)
        self.turn_idx = 0
        
        self.setupUi(self)
        #self.pb_reset.clicked.connect(self.myreset)
        
        # 기본 바둑판 그리기 (pushbutton)  
        self.pb2D = []
        for i in range(10) :
            line = []
            for j in range(10) :
                pb = QPushButton(self)
                pb.setText('')
                pb.setIconSize(QSize(40, 40))
                pb.setGeometry(40*j, 40*i, 40, 40) 
                pb.setIcon(QtGui.QIcon('images/0.png'))
                pb.setToolTip("{},{}".format(i,j))
                pb.clicked.connect(self.myclick)
                line.append(pb) 
            self.pb2D.append(line)
        self.myrender()
    
    # arr2D 값에 따라 pb2D의 pb 이미지 변경         
    def myrender(self):
        for i in range(10) :
            for j in range(10) :
                val = self.arr2D[i][j]
                if val == 0 : 
                    self.pb2D[i][j].setIcon(QtGui.QIcon('images/0.png'))
                elif val == 1 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('images/1.png'))
                elif val == 2 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('images/2.png'))
                    
    # pb 클릭 시 arr2D 값 변경     
    def myclick(self):
        
        pb = self.sender()
        tt = pb.toolTip()
        ij_arr = tt.split(',')
        i_val = int(ij_arr[0])
        j_val = int(ij_arr[1])
        
        if self.arr2D[i_val][j_val] != 0 :
            return
        
        self.turn_idx += 1

        if self.turn_idx % 2 == 0 :
            self.arr2D[i_val][j_val] = 1
        else : 
            self.arr2D[i_val][j_val] = 2
            
        self.myrender()
        
    # 초기화
    def myreset(self):
        np_arr2D = np.array(self.arr2D) * 0
        self.arr2D = np_arr2D
        self.myrender()
        
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()