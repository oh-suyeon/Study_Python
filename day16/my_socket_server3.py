import socket 
from _thread import *

def threaded(client_socket, addr): 

    print('Connected by :', addr[0], ':', addr[1]) 

    while True: 
        try:
            data = client_socket.recv(1024)

            if not data: 
                print('Disconnected by ' + addr[0],':',addr[1])
                break

            print('Received from ' + addr[0],':',addr[1] , data.decode())

            for cs in client_sockets :
                cs.send(data) 

        except :
            for idx, cs in enumerate(client_sockets) :
                if cs == client_socket : 
                    client_sockets.pop(idx)
                    print(idx)
            print('Disconnected by ' + addr[0],':',addr[1])
            print("접속자 수 : ",len(client_sockets))
            break
             
    client_socket.close() 

HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT)) 
server_socket.listen() 

client_sockets = []

print('server start')

while True: 
    print('wait')
    client_socket, addr = server_socket.accept() # 붙을 때까지 대기. 붙은 놈의 소켓 정보와 주소를 준다. 
    client_socket.append(client_sockets)
    start_new_thread(threaded, (client_socket, addr)) # 쓰레드에 정보를 넘긴다. 

server_socket.close() 