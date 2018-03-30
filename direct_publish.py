# -*-coding:utf-8-*-
# ���ݹؼ��ֹ㲥��Ϣ
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# ����ͨ��
channel = connection.channel()
# ����exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
severity = sys.argv[1] if len(sys.argv) > 1 else 'error'  # �ؼ�����'error'��������,�ֶ���
message = ''.join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print("[x] Sent %r:%r" % (severity, message))
connection.close()
