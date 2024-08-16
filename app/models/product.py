from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, Float

from app.database import Base


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    title = Column(String(30))
    description = Column(Text())
    price = Column(Float())
    date_time_create = Column(DateTime(), default=datetime.now())
    date_time_update = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())
