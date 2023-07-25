import socket

s = socket.socket()

PORT = 8585
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)


s.bind(ADDR)

def start():
    s.listen(3)
    print("Waiting for connections !!!")
    while True:
        conn, addr = s.accept()
        print("New Conn", addr)
        conn.send(bytes(f"Welcome to network !!!",'utf-8'))
        

start()

