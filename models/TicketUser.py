from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DBSession = scoped_session(sessionmaker())
class _Base(object):
    query = DBSession.query_property()

Base = declarative_base(cls=_Base)

class TicketUser(Base):
    __tablename__ = 'event_user'  # Имя таблицы в базе данных
<<<<<<< HEAD
    id = Column(Integer, primary_key=True)
=======

>>>>>>> origin/stats
    ticket_id = Column(Integer)
    user_id = Column(Integer)
