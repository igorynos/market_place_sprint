from sqlalchemy import Column, Integer, String

from app.database import Base


class Grade(Base):
    __tablename__ = 'grade'

    id = Column(Integer(), primary_key=True)
    title = Column(String(30))
