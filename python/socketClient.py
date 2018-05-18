import socket

clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def receiveMsg():
    return clientSocket.recv(1024)

def clientConn(ip,port):
    clientSocket.connect((str(ip),int(port)))

def sendMsg(x):
    clientSocket.sendall(x)