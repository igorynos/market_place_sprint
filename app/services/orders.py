from sqlalchemy.orm import Session

from app.dto import orders
from app.models.orders import Orders


def create_order(data: orders.Orders, db):
    order = Orders(user_id=data.user_id,
                   shop_id=data.shop_id,
                   product_id=data.product_id,
                   status_id=data.status_id,
                   )

    try:
        db.add(order)
        db.commit()
        db.refresh(order)
    except Exception as error:
        print(error)

    return order


def get_order(id: int, db):
    return db.query(Orders).filter(Orders.id == id).first()


def update(data: orders.Orders, db: Session, id: int):
    order = db.query(Orders).filter(Orders.id == id).first()

    for params in data:
        order.params = params

    try:
        db.add(order)
        db.commit()
        db.refresh(order)
    except Exception as error:
        print(error)

    return order


def remove(id: int, db: Session):
    order = db.query(Orders).filter(Orders.id == id).delete()
    db.commit()
    return order






