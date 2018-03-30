# greenlet是一个用C实现的协程模块,相比与python自带的yield,它可以使你在任意函数
# 之间随意切换,而不需要把这个函数先声明为generator
# greenlet全部运行在主程序操作系统进程的内部,但它们被协作式地调度
from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()