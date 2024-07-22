from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKeyConstraint

from app.database import Base


class Cards(Base):
    __tablename__ = 'cards'

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer())
    product_id = Column(Integer())

    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id']),
        ForeignKeyConstraint(['product_id'], ['products.id']),
    )