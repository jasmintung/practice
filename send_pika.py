# -*-coding:utf-8-*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # �൱�ڴ���socket
channel = connection.channel()  # �൱�ڹܵ�

# ����queue
channel.queue_declare(queue='hello')  # ����������hello
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print("[x] Sent 'Hello World!'")
connection.close()
