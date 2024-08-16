import pika

from app.config import load_config

config = load_config()
# создание подключения(connection) и канала(channel)
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=config['rmq_host'],
    port=config['rmq_port']
))
channel = connection.channel()


# шаблон для отправки сообщения
# принимает exchange(Название exchange), router(название очереди), body(тело сообщения(json или str))
def message_orders(exchange, router, body):
    channel.basic_publish(exchange=exchange,
                          routing_key=router,
                          body=body
                          )


# создааёт обменники(exchange), очереди(queue), и связывает их между собой
channel.exchange_declare(exchange='orders', exchange_type='direct')
channel.queue_declare(queue='new_orders')
channel.queue_declare(queue='processing_orders')
channel.queue_declare(queue='notification_orders')
channel.queue_bind(exchange='orders', queue='new_orders')
channel.queue_bind(exchange='orders', queue='processing_orders')
channel.queue_bind(exchange='orders', queue='notification_orders')
