import sys
from PyQt5 import uic, QtGui
from PyQt5.Qt import QSize
from PyQt5.QtWidgets import *
from conda.common._logic import TRUE
from networkx.generators import line
import socket 
import threading
import time


form_class = uic.loadUiType("myomok_network.ui")[0]

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
        
        # 차례 정하기
        self.index = 1
        self.flag_wb = False
        # 게임이 진행 중인지 여부
        self.flag_ing = False
        
        # 네트워크 소켓 연결
        self.cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        self.cs.connect(('192.168.42.92', 9999))
        
        # designer에서 그린 것 가져오기
        self.setupUi(self)
        self.pb_reset.clicked.connect(self.myreset)
        self.pb_start.clicked.connect(self.mystart)
        
        # 기본 바둑판 그리기 (pushbutton)  
        self.pb2D = []
        for i in range(19) :
            line = []
            for j in range(19) :
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
    
        # 네트워크 쓰레드 실행 (네트워크는 화면 세팅 다 되고 하는 게 좋음)
        self.my_t1 = threading.Thread(target=self.recv_thread)
        self.my_t1.start()
    
    
    def recv_thread(self):
        while True: 
            data = self.cs.recv(1024) 
            command_q = repr(data.decode())
            command = command_q.replace("'","")
            c_arr = command.split(",") 
            if c_arr[0]=="start" :
                self.net_start()
            elif c_arr[0]=="putstone":
                self.net_putstone(int(c_arr[1]),int(c_arr[2]),int(c_arr[3]))
                    
        
    def net_putstone(self,i,j,stone):
        
        self.arr2D[i][j] = stone
        
        # 결과 출력
        up = self.getUP(i,j,stone)
        dw = self.getDW(i,j,stone)
        ri = self.getRI(i,j,stone)
        le = self.getLE(i,j,stone)

        ul = self.getUL(i,j,stone)
        ur = self.getUR(i,j,stone)
        dl = self.getDL(i,j,stone)
        dr = self.getDR(i,j,stone)
        
        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = ri + le + 1
        d4 = ul + dr + 1
        
        self.myrender()
        
        if d1==5 or d2==5 or d3==5 or d4==5 :
            if stone == 1 :
                QMessageBox.information(self, '오목', '[백] 돌 승리')
            elif stone == 2 :
                QMessageBox.information(self, '오목', '[흑] 돌 승리')
        
            self.flag_ing = False
            
        self.index += 1
        
        
    def net_start(self):
        self.flag_ing = True
        self.pb_start.setEnabled(False)
        
    def __del__(self):
        self.cs.close() 
    
    def mystart(self):
        self.flag_wb = True
        # 서버에 "start," 를 보내기 (나중에 쪼개서 쓸 거라 , 붙이기)
        command = "start,"
        self.cs.send(command.encode())
    
    
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
                    
    
    # pb 클릭 시 서버에 값 전달   
    def myclick(self):
        if not self.flag_ing : 
            return
        
        pb = self.sender()
        tt = pb.toolTip()
        ij_arr = tt.split(',')
        i_val = int(ij_arr[0])
        j_val = int(ij_arr[1])
        
        if self.arr2D[i_val][j_val] > 0 :
            return
    
        stone = -1
        stone_mod = -1
        if self.flag_wb :
            stone = 1
            stone_mod = 1
        else : 
            stone = 2
            stone_mod = 0
            
        # 자기 차례가 아니면 놓을 수 없음
        if self.index % 2 != stone_mod :
            return 
    
        command = "putstone,{},{},{}".format(i_val,j_val,stone)
        self.cs.send(command.encode())
                    
                    
    def myclick__(self):
        # 게임이 끝났을 때는 return (self.flag_ing)
        if not self.flag_ing : 
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
            
            self.flag_ing = False

    
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
        self.flag_ing = True
        
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