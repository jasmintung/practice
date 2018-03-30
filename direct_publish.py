# -*-coding:utf-8-*-
# 根据关键字广播消息
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 创建通道
channel = connection.channel()
# 声明exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
severity = sys.argv[1] if len(sys.argv) > 1 else 'error'  # 关键字是'error'还是其它,手动改
message = ''.join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print("[x] Sent %r:%r" % (severity, message))
connection.close()
