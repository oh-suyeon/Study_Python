import sys
from PyQt5 import uic, QtGui
from PyQt5.Qt import QSize
from PyQt5.QtWidgets import *
from conda.common._logic import TRUE
from networkx.generators import line
from ursina import *

form_class = uic.loadUiType("myomok02.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        
        # 칸의 상태 (0, 1, 2)
        self.arr2D = [
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                                                  
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
    
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                                                  
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0]
            ]        
        
        # 돌을 둘 차례를 정하기 
        self.flag_wb = True
        # 게임이 끝났는지 여부 
        self.flag_end = False
        # designer에서 그린 것 가져오기
        self.setupUi(self)
        self.pb_reset.clicked.connect(self.myreset)
        # 기본 바둑판 그리기 (pushbutton)  
        self.pb2D = []
    
    # arr2D 값에 따라 pb2D의 pb 이미지 변경         
    def myrender(self):
        for i in range(19) :
            for j in range(19) :
                val = self.arr2D[i][j]
                if val == 0 : 
                    self.pb2D[i][j].setIcon(QtGui.QIcon('images/0.png'))
                elif val == 1 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('images/1.png'))
                elif val == 2 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('images/2.png'))
                    
    # pb 클릭 시 arr2D 값 변경     
    def myclick(self):
        
        # 게임이 끝났을 때는 return (self.flag_ing)
        if self.flag_end : 
            return
        
        pb = self.sender()
        tt = pb.toolTip()
        ij_arr = tt.split(',')
        i_val = int(ij_arr[0])
        j_val = int(ij_arr[1])
        
        if self.arr2D[i_val][j_val] > 0 :
            return
        
        stone = -1
        if self.flag_wb :
            self.arr2D[i_val][j_val] = 1
            stone = 1
        else : 
            self.arr2D[i_val][j_val] = 2
            stone = 2
        
        # 결과 출력
        up = self.getUP(i_val,j_val,stone)
        dw = self.getDW(i_val,j_val,stone)
        ri = self.getRI(i_val,j_val,stone)
        le = self.getLE(i_val,j_val,stone)

        ul = self.getUL(i_val,j_val,stone)
        ur = self.getUR(i_val,j_val,stone)
        dl = self.getDL(i_val,j_val,stone)
        dr = self.getDR(i_val,j_val,stone)
        
        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = ri + le + 1
        d4 = ul + dr + 1
        
        self.myrender()
        
        if d1==5 or d2==5 or d3==5 or d4==5 :
            if self.flag_wb :
                QMessageBox.information(self, '오목', '[백] 돌 승리')
            else :
                QMessageBox.information(self, '오목', '[흑] 돌 승리')
            
            self.flag_end = True

        self.flag_wb = not self.flag_wb
        
    
    # 돌이 일렬로 놓인 수를 세는 메서드를 만들기  
    def getUP(self, i, j, stone):
        cnt = 0
        try:
            while True :
                i -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone : 
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
            
    def getDW(self, i, j, stone):
        cnt = 0
        try:
            while True :
                i += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone : 
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def getRI(self, i, j, stone):
        cnt = 0
        try:
            while True :
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone : 
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def getLE(self, i, j, stone):
        cnt = 0
        try:
            while True :
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone : 
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def getUR(self, i, j, stone):
        cnt = 0
        try:
            while True :
                i -= 1
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone : 
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def getDL(self, i, j, stone):
        cnt = 0
        try:
            while True :
                i += 1
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone : 
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def getUL(self, i, j, stone):
        cnt = 0
        try:
            while True :
                i -= 1
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone : 
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def getDR(self, i, j, stone):
        cnt = 0
        try:
            while True :
                i += 1
                j += 1
                if i < 0 :
                    return 
                if j < 0 :
                    return 
                if self.arr2D[i][j] == stone : 
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
    
    # 초기화
    def myreset(self):
        self.flag_wb = True
        self.flag_end = False
        
        # self.arr2D을 새로 만든다거나 하면 위험
        # 배열 안에 들어있는 건 값이 아니라 주소지라서
        # for문 돌면서 0을 넣어주는 게 좋다
        for i in range(19) : 
            for j in range(19) :
                self.arr2D[i][j] = 0
        
        self.myrender()
        
        
        
        
        
        
        
        
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()