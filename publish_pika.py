# -*-coding:utf-8-*-
# 消息发布
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 创建通道
channel = connection.channel()
# 定义exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')
message = ''.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print("[x] Sent %r" % message)
connection.close()
