from sqlalchemy import Column, Integer, String

from app.database import Base


class Order_status(Base):
    __tablename__ = 'order_status'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
