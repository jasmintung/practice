# 让线程延时运行

import threading


def hello():
    print("hello, world")


t = threading.Timer(30.0, hello)
t.start()  # after 30 seconds, "hello world" will be printed
