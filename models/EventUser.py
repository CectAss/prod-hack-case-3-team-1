from sqlalchemy import Column, Integer, String, TIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'event_user'  # Имя таблицы в базе данных

    event_id = Column(Integer)
    user_id = Column(Integer)
