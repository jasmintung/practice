# -*-coding:utf-8-*-
# 更细致的消息过滤，有点正则的意思
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
binding_keys = sys.argv[1:]
print(binding_keys)
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)
for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)
print("[x] Waiting for logs. To exit press ....")


def callback(ch, method, properties, body):
    print("[x] %r:%r" % (method.routing_key, body))  # method.routing_key是生产者的routing_key, body是生产者body

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()
