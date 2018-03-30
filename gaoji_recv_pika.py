# -*-coding:utf-8-*-
import pika, time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()  # ����ͨ��

channel.queue_declare(queue='task_queue', durable=True)  # �������в��־û�,�������߱���һ��
print("[*] Waiting for message. To exit press cc..")


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)  # ���յ�������
    time.sleep(10)
    print("[x] Done")
    print("method.delivery_tag", method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)
# Ĭ����Ϣ������������ǰ���˳�����������ߣ����磺������1ȥ�����л�ȡ ���� ���е�����
# ������2ȥ�����л�ȡ ż�� ���е�����
# ���д󲿷������,��Ϣ���к�˵������߷������Ĵ��������ǲ���ͬ��,
# ��ͻ�����еķ���������ʱ��ϳ�,��Դ�˷ѵ����,��ô,���Ǿ���Ҫ�ı�Ĭ�ϵ���Ϣ���л�ȡ˳��
channel.basic_qos(prefetch_count=1)  # ��ƽ�ַ�, ��ʾ˭��˭ȡ�����ٰ�����ż������
# no_ack = False:��ʾ�������Ժ�������״̬֪ͨRabbitMQ,
# ����������������(its channel is closed, connection is closed, or TCP connection is lost)�ҵ��ˣ���ô��RabbitMQ�����½���������ӵ�������
channel.basic_consume(callback, queue='task_queue')

channel.start_consuming()
