from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKeyConstraint

from app.database import Base


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer())
    shop_id = Column(Integer())
    product_id = Column(Integer())
    status_id = Column(Integer())
    date_time_create = Column(DateTime(), default=datetime.now())
    date_time_update = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())

    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id']),
        ForeignKeyConstraint(['shop_id'], ['shops.id']),
        ForeignKeyConstraint(['product_id'], ['products.id']),
        ForeignKeyConstraint(['status_id'], ['order_status.id']),
    )
