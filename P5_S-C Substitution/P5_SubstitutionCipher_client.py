import socket
from P5utils import *

c = socket.socket()
port = 8787


c.connect(('localhost',port))
while 1:
    msg = input('Enter your message : ')
    key = input('Enter your key : ')
    encrypted_msg = enkrypt(msg,int(key))
    print("Cipher Text send to Server : ",encrypted_msg)
    if msg==";" :
        c.close()
        break
    
    c.send(bytes(encrypted_msg,'utf-8'))

    decrypted_msg = c.recv(1024).decode()
    print(f"Decrypted msg {decrypted_msg}")