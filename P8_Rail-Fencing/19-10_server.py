def decryptRailFence(cipher, key):

    rail = [['\n' for i in range(len(cipher))]for j in range(key)]
    dir_down = None
    row, col = 0, 0 
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        rail[row][col] = '*'
        col += 1
         
        if dir_down:
            row += 1
        else:
            row -= 1
             
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

import socket


def server_program():
    host = socket.gethostname() 
    port = 5000  

    server_socket = socket.socket()  
    server_socket.bind((host, port)) 

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()   #encrypted data
        if not data:
            break
        print("From connected user: " + str(data))  #printing encrypted data
        key=(int(input("Enter the key to decrypt :: ")))
        data=decryptRailFence(data,key)  # decrypting the data
        print("Decrypted Message :: ", data)
        conn.send(data.encode())  # send decrypted data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()