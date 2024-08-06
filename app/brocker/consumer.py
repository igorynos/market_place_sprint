import json

import pika
from sqlalchemy import desc

from app.brocker.producer import message_orders
from app.database import SessionLocal
from app.dto.orders import Orders as OrdersDTO
from app.models.cards import Cards
from app.models.orders import Orders
from app.models.product import Products
from app.models.shops import Shops
from app.models.users import Users
from app.services import orders as ServiceOrder


# принимает сообщение(body) от exchange: orders по routingkey: processing_orders
# проверяет условия для создания заказа, создает новый заказ, даёт ему статус(Новый)
def new_orders_callback(ch, method, properties, body):
    try:
        body = json.loads(body.decode('utf-8'))
        with SessionLocal() as db:
            db.query(Users).filter(Users.id == body['user_id']).first()
            db.query(Shops).filter(Shops.id == body['shop_id']).first()
            db.query(Products).filter(Products.id == body['product_id']).first()
        body['status_id'] = 1
        ServiceOrder.create_order(OrdersDTO(**body), db)
        body = json.dumps(body)
        message_orders('orders', 'processing_orders', body=body)
    except Exception as error:
        print(f'Произошла ошибка данных: {error}')


# принимает сообщение(body) от exchange: orders по routingkey: new_orders
# обрабатывает заказ, меняет его статус(В обработке) и добавляет его в корзину клиента
def processing_orders_callback(ch, method, properties, body):
    try:
        body = json.loads(body.decode('utf-8'))
        with SessionLocal() as db:
            card = Cards(user_id=body['user_id'],
                         product_id=body['product_id'],
                         )
            db.add(card)
            db.commit()
            db.refresh(card)
        body['status_id'] = 2
        body = json.dumps(body)
        message_orders('orders', 'notification_orders', body=body)
    except Exception as error:
        print(f'Произошла ошибка данных: {error}')


# принимает сообщение(body) от exchange: orders по routingkey: notification_orders
# отправляет уведомление о заказе по номеру клиента.
def notification_orders_callback(ch, method, properties, body):
    try:
        body = json.loads(body.decode('utf-8'))
        with SessionLocal() as db:
            user = db.query(Users).filter(Users.id == body['user_id']).first()
            order = db.query(Orders).order_by(desc(Orders.id)).filter(Orders.user_id == body['user_id']).first()
        print(f'Ваш заказ №{order.id} ждёт отправки. \n'
              f'Уведомление на номер: {user.phone_number}')
    except Exception as error:
        print(f'Произошла ошибка данных: {error}')


# Создаёт подключение(connection), канал(channel), и обрабатывает сообщения с модуля producer
# запускается в pool_list модуля main.py
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='new_orders')
    channel.queue_declare(queue='processing_orders')
    channel.queue_declare(queue='notification_orders')

    channel.basic_consume(queue='new_orders',
                          auto_ack=True,
                          on_message_callback=new_orders_callback)

    channel.basic_consume(queue='processing_orders',
                          auto_ack=True,
                          on_message_callback=processing_orders_callback)

    channel.basic_consume(queue='notification_orders',
                          auto_ack=True,
                          on_message_callback=notification_orders_callback)

    channel.start_consuming()
