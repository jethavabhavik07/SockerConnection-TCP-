
import socket

port = 7000  # socket server port number
IP = socket.gethostname()
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
client_socket.connect((IP, port))  # connect to the server

message = input('->')
while message.lower().strip() != 'bye':
    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response

    print('Received from server: ' + data)  # show in terminal

    message = input(" -> ")  # again take input

client_socket.close()  # close the connection


# if __name__ == '__main__':
    # client_program()
