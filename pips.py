# 不同进程间内存是不共享的，要想实现两个进程间的数据交换，可用以下方法：之管道
from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, "hello"])
    conn.close()

if __name__ == '__main__':
    parent_conn, chile_conn = Pipe()
    p = Process(target=f, args=(chile_conn, ))
    p.start()
    print(parent_conn.recv())
    p.join()
