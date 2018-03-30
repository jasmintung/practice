import select
import socket
import sys
import queue


server = socket.socket()
server.setblocking(False)  # 设置socket为非阻塞

server_addr = ('localhost', 10000)

print('starting up on %s port %s' % server_addr)
server.bind(server_addr)  # 绑定端口,IP

server.listen(5)  # 在拒绝连接前,操作系统可以挂起的最大连接数量,限制了 一个时刻 服务器最多接收的客户端

inputs = [server, ]  # 自己也要监测,因为server本身是个fd
outputs = []

message_queues = {}

while True:
    print("waiting for next event...")
    readable, writeable, exeptional = select.select(inputs, outputs, inputs)  # 如果没有任何fd
    # 就绪,那程序就会一直阻塞在这里,readable表示存就绪的socket fd,exeptional表示存放异常的fd
    for s in readable:  # 每个s就是一个socket

        if s is server:  # 上面server自己也当做一个fd放在了inputs列表里,传给了select,如果这个s是server,代表server这个fd就绪了
            # 就是有活动了,什么情况下它才有活动?当然 是有新的连接进来的时候!
            # 新连接进来了,接受这个连接
            conn, client_addr = s.accept()
            print("new connection from", client_addr)
            conn.setblocking(False)
            inputs.append(conn)  # 为了不阻塞整个程序,我们不会离开在这里开始接收客户端发来的数据,把它放到inputs里,下一次loop时,
            # 这个新连接就会被交给select去监听,如果这个连接的客户端发来了数据,那么这个连接的fd在server端就会变成就绪的,select就会把
            # 这个连接返回,返回到 readable 列表里面,取出这个连接,开始接收数据了,下面就是这么干的
            message_queues[conn] = queue.Queue()  # 接收到客户端的数据后,不立刻返回,暂时在队列里,以后发送
        else:  # s不是 server 的话,那就只能是一个 与客户端建立连接的fd了
            # 客户端的数据过来了,在这接收
            data = s.recv(1024)
            if data:
                print("收到来自[%s]的数据:" % s.getpeername()[0], data)
                message_queues[s].put(data)  # 收到的数据先放到queue里,一会儿返回给客户端
                if s not in outputs:
                    outputs.append(s)
            else:  # 收不到data,客户端断开
                print("客户端断开了")
                if s in outputs:
                    outputs.remove(s)  # 清理已断开的连接
                inputs.remove(s)  # 清理已断开的连接
                del message_queues[s]  # 清理已断开的连接
    for s in writeable:
        try:
            next_msg = message_queues[s].get_nowait()

        except queue.Empty:
            print("client [%s]" % s.getpeername()[0], "queue is empty..")
            outputs.remove(s)
        else:
            print("sending msg to [%s]" % s.getpeername()[0], next_msg)
            s.send(next_msg.upper())

    for s in exeptional:
        print("handling exception for", s.getpeername())
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        del message_queues[s]
