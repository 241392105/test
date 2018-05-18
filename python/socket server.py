import socket
import threading
from time import ctime,sleep

def rec():
    while True:
        sleep(0.2)
        try:
            print("client:"+conn.recv(1024))
        except:
            continue
def send():
    while True:
        sleep(0.2)
        try:
            conn.sendall(raw_input())
        except:
            continue

host="127.0.0.1"
port=11110
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind((host,port))
soc.listen(10)
print("start")
while True:
    try:
        conn,addr=soc.accept()
        t1=threading.Thread(target=rec)
        t1.setDaemon(True)
        t1.start()
        t2=threading.Thread(target=send)
        t2.setDaemon(True)
        t2.start()
    except:
        continue