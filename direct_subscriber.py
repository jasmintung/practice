# -*-coding:utf-8-*-
# 根据关键字接收消息 routing_key
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 创建通道
channel = connection.channel()
# 声明exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# severities = sys.argv[1:]
severities = ['error', 'info', ]
# if not severities:
#     sys.stderr.write("Usage: %s [info][warning][error]\n" % sys.argv[0])
#     sys.exit(1)
for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)
print('[*] Waiting for logs. To exit press ....')


def callback(ch, method, properties, body):
    print("[x] %r:%r" % (method.routing_key, body))
channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()