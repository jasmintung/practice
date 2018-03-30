# 守护线程 ,join的作用是等待线程执行完成
import time
import threading


def run(n):

    print('[%s]------running------\n' % n)
    time.sleep(2)
    print('---done---')


def main():
    for i in range(5):
        print(i)
        t = threading.Thread(target=run, args=[i, ])
        t.start()
        t.join(1)
        print('starting thread', t.getName())

m = threading.Thread(target=main, args=[])
m.setDaemon(True) # 将main线程设置为Daemon线程，它作为程序主线程的守护线程，当主程序退出时，m线程也会退出，由m启动的其它子线程也会退出，不管事发后执行任务,如果不写这个,意味着主线程执行完成，子线程如果没有执行完成，照常执行
m.start()
start_time = time.time()
m.join(timeout=2)  # 等待2秒让其执行完成
end_time = time.time()
print(end_time-start_time)
print("---main thread done---")
