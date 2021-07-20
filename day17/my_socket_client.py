import socket 
import threading
import time

def recv_thread(cs):
    while True: 
        data = cs.recv(1024) # hold
        print('\nReceived from the server :',repr(data.decode())) 


def send_thread(cs):
    while True: 
        message = input('Enter Message : ') # hold
        if message == 'quit':
            break
        txt = "{}:{}".format(cs.getsockname()[0], message)
        cs.send(txt.encode()) 
        

# HOST = '192.168.42.149'
HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
client_socket.connect((HOST, PORT))

# send
my_t1 = threading.Thread(target=send_thread,args=(client_socket,)) 
my_t1.start() 
my_t1.join()

# receive
my_t2 = threading.Thread(target=recv_thread,args=(client_socket,)) 
my_t2.start() 
my_t2.join()

# 무한 루프를 돌려줘야 쓰레드가 끝나지 않음 (join으로 대체가능)
# gui에서는 join이나 무한루프는 필요 없음. 콘솔은 자동으로 꺼지지만 gui는 계속 켜져있으니까
# while True : 
#     time.sleep(1)
#     pass

client_socket.close() 