def encryptRailFence(text, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))


import socket
def client_program():
    host = socket.gethostname()  
    port = 5000 

    client_socket = socket.socket()  
    client_socket.connect((host, port)) 

    message = input("INPUT -> ")
    key=(int(input("Enter The Key :: ")))
    
    while message.lower().strip() != 'exit':
        client_socket.send(encryptRailFence(message,key).encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server :: ' + data)  # show in terminal

        message = input("INPUT -> ")  # again take input
        key=(int(input("Enter the key :: ")))
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()