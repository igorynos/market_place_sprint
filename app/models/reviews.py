from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKeyConstraint, Text, DateTime, String

from app.database import Base


class Reviews_products(Base):
    __tablename__ = 'reviews_products'

    id = Column(Integer(), primary_key=True)
    product_id = Column(Integer())
    title = Column(String(30))
    description = Column(Text())
    grade_id = Column(Integer())
    date_time_create = Column(DateTime(), default=datetime.now())

    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['products.id']),
        ForeignKeyConstraint(['grade_id'], ['grade.id']),
    )


class Reviews_shops(Base):
    __tablename__ = 'reviews_shops'

    id = Column(Integer(), primary_key=True)
    shop_id = Column(Integer())
    title = Column(String(30))
    description = Column(Text())
    grade_id = Column(Integer())
    date_time_create = Column(DateTime(), default=datetime.now())

    __table_args__ = (
        ForeignKeyConstraint(['shop_id'], ['shops.id']),
        ForeignKeyConstraint(['grade_id'], ['grade.id']),
    )
