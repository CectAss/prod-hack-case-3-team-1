from sqlalchemy import Column, Integer, String, TIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'event'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Столбец id, первичный ключ
    spending = Column(Integer)  # Столбец username, не может быть null
    reason = Column(String)
    date = Column(TIME, nullable=False)
