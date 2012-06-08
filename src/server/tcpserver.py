from socket import *
from time import ctime
import threading
HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)
def server(address, size):
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(address)
    tcpSerSock.listen(5)

    while True:
        print("waiting for connecting!")
        tcpcliSock, addr = tcpSerSock.accept()
        print('...connect from:', addr)

        while True:
            data = tcpcliSock.recv(size)
            if not data:
	        break
            tcpcliSock.send('[%s] %s' % (ctime(), data))
        tcpcliSock.close()
    tcpSerSock.close()
if __name__ == '__main__':
    threads = []
    for i in range(5):
        ADDR = (HOST, PORT + i)
	t = threading.Thread(target = server, args = (ADDR, BUFSIZE))
	threads.append(t)
	t.start()

     
