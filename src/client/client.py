from socket import *
import sys
HOST = 'localhost'
BUFSIZE = 1024
PORT = 21568

def client_socket():
    ADDR = (HOST, PORT)
    tcpclisock = socket(AF_INET, SOCK_STREAM)
    tcpclisock.connect(ADDR)

    while True:
        data = raw_input('>')
        if not data:
            break
        tcpclisock.send(data)
        data = tcpclisock.recv(BUFSIZE)
        if not data:
            break
        print(data)

    tcpclisock.close()
if __name__ == '__main__':
    client_socket()
   
