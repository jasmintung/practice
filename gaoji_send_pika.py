# -*-coding:utf-8-*-
import pika
import time
import sys

# 创建socket
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 创建通道
channel = connection.channel()

# 创建消息队列
channel.queue_declare(queue='task_queue', durable=True)  # durable 声明队列并持久化

message = ''.join(sys.argv[1:]) or "Hello World! %s" % time.time()
channel.basic_publish(exchange='', routing_key='task_queue', body=message,
                      properties=pika.BasicProperties(delivery_mode=2)  # 消息持久化
                      )
print("[x] Sent %r" % message)
connection.close()
