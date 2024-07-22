from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKeyConstraint

from app.database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(30))
    second_name = Column(String(30))
    email = Column(String(30))
    phone_number = Column(String(15))
    address_id = Column(Integer())
    date_birth = Column(Date())
    date_time_create = Column(DateTime(), default=datetime.now())
    date_time_update = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())

    __table_args__ = (
        ForeignKeyConstraint(['address_id'], ['address.id']),
    )
