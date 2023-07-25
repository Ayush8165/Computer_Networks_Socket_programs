import socket
import threading
import os
import json
import time


# constants

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 1024
DISCONNECTION_MSG = ';;'
FORMAT = 'utf-8' 
CONNECTIONS = []
ConnName = {}
# making a server connection
server = socket.socket()
server.bind(ADDR)   #binding our server to address

print('[Initialising] Socket has been initialised ....')


# utility to handle clients

def handle_client(conn, addr):
    print('[New Connection]', addr, 'connected.')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECTION_MSG:
                print(addr, 'has disconnected safely.')
                connected = False
            name = ConnName[conn]
            msg = name + " : " + msg
            for cli in CONNECTIONS:
                if cli!=conn:
                    cli.send(bytes(msg,FORMAT))
            # print(addr, msg)
            # conn.send(bytes(data,FORMAT))

    conn.close()    # safely closing the connection


# start function


def start():
    print(f'[Starting] Server has been running on {ADDR}')
    server.listen()
    print('[Listening] Waiting for clients') 
    
    while True:
        conn, addr = server.accept()
        CONNECTIONS.append(conn)
        name  = conn.recv(1024).decode(FORMAT)
        ConnName[conn] = name
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # used threading to make handling of clients async
        thread.start()  #starting a new thread every time new clients join


start()