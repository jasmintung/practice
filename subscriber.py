# -*-coding:utf-8-*-
# 消息订阅
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 创建通道
channel = connection.channel()
# 定义exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')
# 声明队列
result = channel.queue_declare(exclusive=True)  # 不指定queue名字,RabbitMQ会随机分配一个名字,
# exclusive=True会在使用此queue的消费者断开后，自动将queue删除
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)
print('[*] Waiting for logs. To exit press ....')


def callback(ch, method, properties, body):
    print("[x] %r" % body)

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()