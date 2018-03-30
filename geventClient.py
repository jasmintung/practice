# 通过gevent实现单线程下的多socket并发
import socket

HOST = 'localhost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = bytes(input(">>"), encoding="utf-8")
    s.sendall(msg)
    data = s.recv(1024)

    print('Received', data)
s.close()
