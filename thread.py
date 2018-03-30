import threading
import time


def rollback():
    sayhi(9)


def sayhi(num):
    print("running on number:%s" % num)
    rollback()
    time.sleep(3)

if __name__ == '__main__':
    t1 = threading.Thread(target=sayhi, args=(1, ))
    t2 = threading.Thread(target=sayhi, args=(2, ))
    t1.start()
    t2.start()
    print(t1.getName())
    print(t2.getName())

# # 继承调用
#
# import threading
# import time
#
#
# class MyThread(threading.Thread):
#     def __init__(self, num):
#         threading.Thread.__init__(self)
#         self.num = num
#
#     def run(self):  # 定义每个线程要运行的函数
#         while True:
#             print("running on number:%s" % self.num)
#             time.sleep(3)
#
# if __name__ == '__main__':
#     t1 = MyThread(1)
#     t2 = MyThread(2)
#     t1.start()
#     t2.start()
