# 进程池
from multiprocessing import Process, Pool
import time
import os

def Foo(i):
    time.sleep(2)
    print(os.getpid())
    print("i=%d", i)
    return i+100


def Bar(args):
    print(os.getpid())
    print("exec done:", args)

if __name__ == '__main__':
    print(os.getpid())
    pool = Pool(5)
    for i in range(10):
        pool.apply_async(func=Foo, args=(i, ), callback=Bar)  # callback=Bar是回调，表示Foo执行完成后返回的时候在主线程执行Bar
        # pool.apply(func=Foo, args=(i, ))
    print("end")
    pool.close()
    pool.join()  # 进程池中进程执行完毕再关闭,如果注释,那么程序直接关闭
