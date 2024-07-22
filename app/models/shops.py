from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text

from app.database import Base


class Shops(Base):
    __tablename__ = 'shops'

    id = Column(Integer(), primary_key=True)
    name = Column(String(30))
    description = Column(Text())
    email = Column(String(30))
    phone_number = Column(String(15))
    date_time_create = Column(DateTime(), default=datetime.now())
    date_time_update = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())
