import socket
 
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
 
def originalText(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))
 
 
 
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
 
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
 
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("\n")
        print('20BCS018 AYUSH CHAUHAN')
        print("\n")
        print("Encrypted message: ")
        print(data)
        keyword=input("Enter keyword set on client side to decrypt message: ")
        key = generateKey(data, keyword)
        print("Decrypted Text :",originalText(data, key))
        Decrypted=originalText(data, key)
        # print("from connected user: " + str(Decrypted))       
 
 
 
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client
 
    conn.close()  # close the connection
 
 
if __name__ == '__main__':
   server_program()