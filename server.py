import socket
#import time

# def server_program():
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 7000
	#maxConnection = 999
IP = socket.gethostname()
s.bind((IP,port))
s.listen(2)
print("Server Up and Running ..... at On Port "+ str(port))

(clientS, address) = s.accept()
print("Connection Made")	
while True:
	message = clientS.recv(1024).decode()
	# if not message:
	# 	break
	print("From Connected User => " + str(message))
	data = input(" -> ")
	clientS.send(data.encode())

clientS.close()

# if __name__ == '__main__':
# 	server_program()



