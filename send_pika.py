# -*-coding:utf-8-*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # 相当于创建socket
channel = connection.channel()  # 相当于管道

# 声明queue
channel.queue_declare(queue='hello')  # 队列名称是hello
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print("[x] Sent 'Hello World!'")
connection.close()
