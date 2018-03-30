# -*-coding:utf-8-*-
import pika
import time
import sys

# ����socket
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# ����ͨ��
channel = connection.channel()

# ������Ϣ����
channel.queue_declare(queue='task_queue', durable=True)  # durable �������в��־û�

message = ''.join(sys.argv[1:]) or "Hello World! %s" % time.time()
channel.basic_publish(exchange='', routing_key='task_queue', body=message,
                      properties=pika.BasicProperties(delivery_mode=2)  # ��Ϣ�־û�
                      )
print("[x] Sent %r" % message)
connection.close()
