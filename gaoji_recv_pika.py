# -*-coding:utf-8-*-
import pika, time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()  # 创建通道

channel.queue_declare(queue='task_queue', durable=True)  # 声明队列并持久化,与生产者保持一致
print("[*] Waiting for message. To exit press cc..")


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)  # 接收到的数据
    time.sleep(10)
    print("[x] Done")
    print("method.delivery_tag", method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)
# 默认消息队列里的数据是按照顺序被消费者拿走，例如：消费者1去队列中获取 奇数 序列的任务，
# 消费者2去队列中获取 偶数 序列的任务。
# 但有大部分情况下,消息队列后端的消费者服务器的处理能力是不相同的,
# 这就会出现有的服务器闲置时间较长,资源浪费的情况,那么,我们就需要改变默认的消息队列获取顺序
channel.basic_qos(prefetch_count=1)  # 公平分发, 表示谁来谁取，不再按照奇偶数排列
# no_ack = False:表示消费完以后不主动把状态通知RabbitMQ,
# 如果消费者遇到情况(its channel is closed, connection is closed, or TCP connection is lost)挂掉了，那么，RabbitMQ会重新将该任务添加到队列中
channel.basic_consume(callback, queue='task_queue')

channel.start_consuming()
