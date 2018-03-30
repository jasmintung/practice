import threading
import time
import random

# 设置一个线程是"门",再设置几个线程为"员工",员工看到门没开，就刷卡,刷完卡，门开了，员工可以通过


def door():
    door_open_time_counter = 0
    while True:
        if door_swiping_event.isSet():
            print("\033[32;1mdoor opening...\033[0m")
            door_open_time_counter += 1
        else:
            print("\033[31;1mdoor closed...., swipe to open.\033[0m")
            door_open_time_counter = 0  # 计时器清空
            door_swiping_event.wait()

        if door_open_time_counter > 3:  # 门已经开了3s了,该关了
            door_swiping_event.clear()

        time.sleep(0.5)


def staff(n):
    print("staff [%s] is coming..." % n)
    while True:
        if door_swiping_event.isSet():
            print("\033[34;1mdoor is opened, passing...\033[0m")
            break
        else:
            print("staff [%s] sees door got closed, swipping the card......" % n)
            print(door_swiping_event.set())
            print("after set", door_swiping_event.set())
        time.sleep(0.5)

door_swiping_event = threading.Event()  # 设置事件
door_thread = threading.Thread(target=door)
door_thread.start()

for i in range(5):
    p = threading.Thread(target=staff, args=(i, ))
    time.sleep(random.randrange(3))
    p.start()
