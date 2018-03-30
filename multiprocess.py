# from multiprocessing import Process
# import time
# import os
#
#
# def f(name):
#     print(os.getppid())
#     time.sleep(2)
#     print("hello", name)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob', ))
#     p.start()
#     print(os.getppid())
#     p.join()
from multiprocessing import Process
import os


def info(title):
    print(title)
    print("module name:", __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("\n\n")


def f(name):
    info("\033[31;1mfunction f\033[0m")
    print("hello", name)

if __name__ == '__main__':
    info("\033[32;1mmain process\033[0m")
    p = Process(target=f, args=("bob", ))
    p.start()
    p.join()
