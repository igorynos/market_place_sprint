from sqlalchemy import Column, Integer, String, ForeignKeyConstraint

from app.database import Base


class Tags_products(Base):
    __tablename__ = 'tags_products'

    id = Column(Integer(), primary_key=True)
    title = Column(String(30))
    product_id = Column(Integer())

    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['products.id']),
    )


class Tags_shops(Base):
    __tablename__ = 'tags_shops'

    id = Column(Integer(), primary_key=True)
    title = Column(String(30))
    shop_id = Column(Integer())

    __table_args__ = (
        ForeignKeyConstraint(['shop_id'], ['shops.id']),
    )