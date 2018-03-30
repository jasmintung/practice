# -*-coding:utf-8-*-
# ��Ϣ����
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# ����ͨ��
channel = connection.channel()
# ����exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')
# ��������
result = channel.queue_declare(exclusive=True)  # ��ָ��queue����,RabbitMQ���������һ������,
# exclusive=True����ʹ�ô�queue�������߶Ͽ����Զ���queueɾ��
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)
print('[*] Waiting for logs. To exit press ....')


def callback(ch, method, properties, body):
    print("[x] %r" % body)

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()