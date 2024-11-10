from models.Event import Event as e
from models.Ticket import Ticket as t
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from mox.Ticket import Ticket
from mox.Event import Event
import datetime

engine = create_engine('sqlite:///hakaton.db')

Session = sessionmaker(bind=engine)
session_db = Session()    

def event_fill(n):
    
    event_arr = [Event().fill(i) for i in range(n)]
    
    for event in event_arr:

        a = e(spending=event.spending, reason=event.reason, date=None)
        session_db.add(a)
        session_db.commit()

def ticket_fill(n):
    
    ticket_arr = [Ticket().fill(i) for i in range(n)]
    
    for ticket in ticket_arr:

        a = t(id=ticket.id, price=ticket.spending, race_number=ticket.race_id, date_arrive=None, date_comeback=None, home=ticket.home, away=ticket.away)
        session_db.add(a)
        session_db.commit()

ticket_fill(15)