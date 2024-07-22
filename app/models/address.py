from sqlalchemy import Column, Integer, String, ForeignKeyConstraint

from app.database import Base


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer(), primary_key=True)
    build = Column(String(30))
    apartment = Column(String(30))
    street_id = Column(Integer())

    __table_args__ = (
        ForeignKeyConstraint(['street_id'], ['streets.id']),
    )


class Streets(Base):
    __tablename__ = 'streets'

    id = Column(Integer(), primary_key=True)
    street_name = Column(String(30))
    city_id = Column(Integer())

    __table_args__ = (
        ForeignKeyConstraint(['city_id'], ['cities.id']),
    )


class Cities(Base):
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True)
    name_city = Column(String(30))
