import socket

c = socket.socket()

PORT = 8585
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

name = input('Enter your name : ')

c.connect(ADDR)
print(c.recv(1024).decode())
c.send(bytes(name,'utf-8'))
