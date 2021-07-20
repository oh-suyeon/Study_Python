import socket 
from _thread import *
import time


#쓰레드 
def threaded(client_socket, addr): 

    print('Connected by :', addr[0], ':', addr[1]) 

    while True: 
        try:
            data = client_socket.recv(1024)

            if not data: 
                print('Disconnected by ' + addr[0],':',addr[1])
                break

            print('Received from ' + addr[0],':',addr[1] , data.decode())
            
            for cs in client_sockets : # 현재 연결된 클라이언트에게 보내기 -> 에코 서버 
                cs.send(data) 

        except : # 클라이언트가 방을 나갔을 때. 
            for idx, cs in enumerate(client_sockets) :
                if cs == client_socket :  
                    client_sockets.pop(idx) # 배열에서 나가기 
                    print("idx",idx)
                    break
                
            print('Disconnected by ' + addr[0],':',addr[1])
            print("접속자 수 : ",len(client_sockets))
            break
             
    client_socket.close() 

HOST = '192.168.42.92'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT)) 
server_socket.listen() 

# 각 메시지는 클라이언트 당 할당된 쓰레드가 전달한다. 
client_sockets = []

print('server start')

while True: 
    print('wait')
    client_socket, addr = server_socket.accept() # 붙을 때까지 대기. 붙은 놈의 소켓 정보와 주소를 준다. (멀티 리턴)
    client_sockets.append(client_socket) # client_socket의 send 메서드를 이용.
    start_new_thread(threaded, (client_socket, addr)) # 쓰레드에 정보를 넘긴다. 
    if len(client_sockets) == 2 :
        break 

while True :
    time.sleep(1)
    pass

server_socket.close() 