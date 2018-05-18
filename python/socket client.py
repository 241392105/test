import socket
import threading
from time import ctime,sleep

def rec():
    while True:
        sleep(0.2)
        try:
            print("server:"+soc.recv(1024))
        except:
            continue

host="127.0.0.1"
port=11110
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect((host,port))
print("conn server")
t1=threading.Thread(target=rec)
t1.setDaemon(True)
t1.start()
while True:
    try:
        soc.sendall(raw_input())
    except:
        break