import threading
import time

num = 0


def sum(i):
    lock.acquire()

    global num
    lock.acquire()

    # time.sleep(1)
    num += i
    lock.release()

    print(num)
    lock.release()


print("%s thread start!" % time.ctime())

try:
    lock = threading.RLock()
    list = []
    for i in range(100):
        t = threading.Thread(target=sum, args=(i, ))
        list.append(t)
        t.start()
        print(t.getName())
    for threadinglist in list:
        threadinglist.join()
except KeyboardInterrupt:
    print("you stop the threading")

print("%s thread end!" % (time.ctime()))

