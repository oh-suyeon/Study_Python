import socket 

HOST = '192.168.42.149'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

client_socket.connect((HOST, PORT)) 

while True: 
    message = input('Enter Message : ')
    if message == 'quit':
        break

    client_socket.send(message.encode()) 

client_socket.close() 