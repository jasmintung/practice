# 最多允许多少个线程同时运行

import threading, time


def run(n):
    semphore.acquire()
    time.sleep(1)
    print("run the thread:%s\n" %n)
    semphore.release()

if __name__ == '__main__':
    num = 0
    semphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(20):
        t = threading.Thread(target=run, args=(i, ))
        t.start()

while threading.active_count() != 1:
    pass
else:
    print("---all threads done---")
    print(num)