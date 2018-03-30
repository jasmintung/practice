import time, random
import queue, threading

# 线程间数据安全传输模型: 生产者消费者模型，它能够解决绝大多数并发问题，通过平衡生产线程和
# 消费线程的工作能力来提供程序的整体处理数据的速度
# 通过一个容器queue来解决生产者和消费者的强耦合问题
# 生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，
# 直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。
q = queue.Queue()


def producer(name):
    count = 0
    while count < 20:
        time.sleep(random.randrange(3))
        q.put(count)
        count += 1
        print("Producer %s has produced %s baozi..." % (name, count))
        print("producer: ", count)


def consumer(name):
    count = 0
    while count < 20:
        time.sleep(random.randrange(4))
        if not q.empty():
            data = q.get()
            print(data)
            print("\033[32;1mCosumer %s has get %s baozi...\033[0m" % (name, data))
        else:
            print("----no baozi anymore----")
        count += 1
        print("consumer: ", count)


def consumer2(name):
    count = 0
    while count < 10:
        time.sleep(random.randrange(3))
        if not q.empty():
            data = q.get()
            print(data)
            print("\033[34;1mConsumer2 % s has get %s baozi...\033[0m" % (name, data))
        else:
            print("-----no baozi anymore-----")
        count += 1
        print("consumer2: ", count)

p1 = threading.Thread(target=producer, args=('A', ))
c1 = threading.Thread(target=consumer, args=('B', ))
c2 = threading.Thread(target=consumer2, args=('C', ))
p1.start()
c1.start()
c2.start()