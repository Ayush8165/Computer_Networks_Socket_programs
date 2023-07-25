# Python code to implement
# Vigenere Cipher
import socket
 
# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
 
# This function returns the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))
 
# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))

 
def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
 
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
 
    message = input("Enter Plain text -> ")  # take input
 
 
    keyword=input("Enter keyword -> ")
    key = generateKey(message, keyword)
    cipher_text = cipherText(message,key)
    print("Ciphertext :", cipher_text)
    # print("Original/Decrypted Text :",originalText(cipher_text, key))
 
 
 
    while message.lower().strip() != 'bye':
        client_socket.send(cipher_text.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print("\n")
        print('20BCS018 AYUSH CHAUHAN')
        print('Received from server: ' + data)  # show in terminal
        print('characters received from server: ')
        message = input(" -> ")  # again take input
 
 
        keyword=input("Enter keyword ")
        key = generateKey(message, keyword)
        cipher_text = cipherText(message,key)
        print("Ciphertext :", cipher_text)
        print("Original/Decrypted Text :",originalText(cipher_text, key))
    client_socket.close()  # close the connection
 
 
if __name__ == '__main__':
    client_program()