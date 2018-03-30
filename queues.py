# 不同进程间内存是不共享的，要想实现两个进程间的数据交换，可用以下方法：之队列
from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, "hello"])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q, ))
    p.start()
    print(q.get())
    p.join()
