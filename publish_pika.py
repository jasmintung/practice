# -*-coding:utf-8-*-
# ��Ϣ����
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# ����ͨ��
channel = connection.channel()
# ����exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')
message = ''.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print("[x] Sent %r" % message)
connection.close()