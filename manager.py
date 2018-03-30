# 进程间资源共享,不同进程对同一个资源进行修改
from multiprocessing import Process, Manager
import os


def f(d, l):
    d[os.getpid()] = os.getpid()
    d['2'] = 2
    d[0.25] = None
    l.append(os.getpid())
    # print(l)

if __name__ == '__main__':
    with Manager() as manage:
        d = manage.dict()

        l = manage.list(range(10))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)
