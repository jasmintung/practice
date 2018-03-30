# 线程锁
import time
import threading

num = 100


def addNum():
    global num
    print('get num:', num)
    time.sleep(1)

    mutex.acquire()  # 加锁
    num -= 1
    print('--num:', num)
    mutex.release()  # 解锁

thread_list = []
mutex = threading.Lock()  # 创建锁
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()  # 等待所有线程执行完毕

print('final num:', num)
