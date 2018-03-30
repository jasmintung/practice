import socket
import sys

messages = [b'This is the message',
            b'It will be sent',
            b'in parts'
           ]

server_address = ('localhost', 10000)

socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM),
         socket.socket(socket.AF_INET, socket.SOCK_STREAM)]

print("connecting to %s port %s" % server_address)
for s in socks:
    s.connect(server_address)

for message in messages:
    for s in socks:
        print('%s: sending "%s"' % (s.getpeername(), message))
        s.send(message)

    for s in socks:
        data = s.recv(1024)
        print('%s: received "%s"' % (s.getpeername(), data))
        if not data:
            print(sys.stderr, 'closing socket', s.getpeername())
