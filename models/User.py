from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Столбец id, первичный ключ
    username = Column(String, nullable=False)     # Столбец username, не может быть null
    password = Column(String,  nullable=False) # password not null
    login = Column(String, nullable=False)
