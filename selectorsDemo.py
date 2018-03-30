import selectors
import socket

sel = selectors.DefaultSelector()


def accept(sock, mask):  # 接入的socket实例
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 10000))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        print("key is :", key)
        print("key data is:", key.data)
        print("key obj is:", key.fileobj)
        print("mask is:", mask)
        callback = key.data  # 是函数accept的地址赋给callback
        callback(key.fileobj, mask)

# 运行的打印如下------------
# 关键词解释:
# SelectorKey：是一个名字数组，用于将一个文件对象关联到它的底层文件描述符、选中的事件掩码和附加的数据。它由几个BaseSelector方法返回。
#       fileobj：文件对象注册,这里是socket实例
#       events：Events that must be waited for on this file object
#       data：与此文件对象相关联的可选的不透明数据:例如，可以用于存储每个客户端会话ID

# key is : SelectorKey(fileobj=<socket.socket fd=204, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000)>, fd=204, events=1, data=<function accept at 0x0000000001D13E18>)
# key data is: <function accept at 0x0000000001D13E18>
# key obj is: <socket.socket fd=204, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000)>
# mask is: 1
# accepted <socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)> from ('127.0.0.1', 5089)

# key is : SelectorKey(fileobj=<socket.socket fd=204, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000)>, fd=204, events=1, data=<function accept at 0x0000000001D13E18>)
# key data is: <function accept at 0x0000000001D13E18>
# key obj is: <socket.socket fd=204, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000)>
# mask is: 1
# accepted <socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)> from ('127.0.0.1', 5090)



# key is : SelectorKey(fileobj=<socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)>, fd=280, events=1, data=<function read at 0x0000000001E80F28>)
# key data is: <function read at 0x0000000001E80F28>
# key obj is: <socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)>
# mask is: 1
# echoing b'This is the message' to <socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)>

# key is : SelectorKey(fileobj=<socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)>, fd=284, events=1, data=<function read at 0x0000000001E80F28>)
# key data is: <function read at 0x0000000001E80F28>
# key obj is: <socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)>
# mask is: 1
# echoing b'This is the message' to <socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)>

# key is : SelectorKey(fileobj=<socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)>, fd=284, events=1, data=<function read at 0x0000000001E80F28>)
# key data is: <function read at 0x0000000001E80F28>
# key obj is: <socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)>
# mask is: 1
# echoing b'It will be sent' to <socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)>

# key is : SelectorKey(fileobj=<socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)>, fd=280, events=1, data=<function read at 0x0000000001E80F28>)
# key data is: <function read at 0x0000000001E80F28>
# key obj is: <socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)>
# mask is: 1
# echoing b'It will be sent' to <socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)>

# key is : SelectorKey(fileobj=<socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)>, fd=284, events=1, data=<function read at 0x0000000001E80F28>)
# key data is: <function read at 0x0000000001E80F28>
# key obj is: <socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)>
# mask is: 1
# echoing b'in parts' to <socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)>

# key is : SelectorKey(fileobj=<socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)>, fd=280, events=1, data=<function read at 0x0000000001E80F28>)
# key data is: <function read at 0x0000000001E80F28>
# key obj is: <socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)>
# mask is: 1
# echoing b'in parts' to <socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)>

# key is : SelectorKey(fileobj=<socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)>, fd=284, events=1, data=<function read at 0x0000000001E80F28>)
# key data is: <function read at 0x0000000001E80F28>
# key obj is: <socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)>
# mask is: 1
# closing <socket.socket fd=284, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5089)>

# key is : SelectorKey(fileobj=<socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)>, fd=280, events=1, data=<function read at 0x0000000001E80F28>)
# key data is: <function read at 0x0000000001E80F28>
# key obj is: <socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)>
# mask is: 1
# closing <socket.socket fd=280, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 10000), raddr=('127.0.0.1', 5090)>


# 客户端的打印
# connecting to localhost port 10000
# ('127.0.0.1', 10000): sending "b'This is the message'"
# ('127.0.0.1', 10000): sending "b'This is the message'"
# ('127.0.0.1', 10000): received "b'This is the message'"
# ('127.0.0.1', 10000): received "b'This is the message'"
# ('127.0.0.1', 10000): sending "b'It will be sent'"
# ('127.0.0.1', 10000): sending "b'It will be sent'"
# ('127.0.0.1', 10000): received "b'It will be sent'"
# ('127.0.0.1', 10000): received "b'It will be sent'"
# ('127.0.0.1', 10000): sending "b'in parts'"
# ('127.0.0.1', 10000): sending "b'in parts'"
# ('127.0.0.1', 10000): received "b'in parts'"
# ('127.0.0.1', 10000): received "b'in parts'"