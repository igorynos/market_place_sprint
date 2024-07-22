from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKeyConstraint, Text, DateTime

from app.database import Base


class Photos_products(Base):
    __tablename__ = 'photos_products'

    id = Column(Integer(), primary_key=True)
    photos = Column(Text())
    product_id = Column(Integer())
    date_time_create = Column(DateTime(), default=datetime.now())

    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['products.id']),
    )


class Photos_shops(Base):
    __tablename__ = 'photos_shops'

    id = Column(Integer(), primary_key=True)
    photos = Column(Text())
    shop_id = Column(Integer())
    date_time_create = Column(DateTime(), default=datetime.now())

    __table_args__ = (
        ForeignKeyConstraint(['shop_id'], ['shops.id']),
    )
