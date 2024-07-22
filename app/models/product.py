from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKeyConstraint, Text

from app.database import Base


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    title = Column(String(30))
    description = Column(Text())
    price = Column(Integer())
    grade_id = Column(Integer())
    date_time_create = Column(DateTime(), default=datetime.now())
    date_time_update = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())

    __table_args__ = (
        ForeignKeyConstraint(['grade_id'], ['grade.id']),
    )
