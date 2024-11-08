from sqlalchemy import Column, Integer, String, TIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'ticket'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Столбец id, первичный ключ
    price = Column(Integer)  # Столбец username, не может быть null
    race_number = Column(String)
    date_arrive = Column(TIME, nullable=False)
    date_comeback = Column(TIME, nullable=False)
    home = Column(String)
    away = Column(String)

