from models.Event import Event as e
from models.Ticket import Ticket as t
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from mox.Ticket import Ticket
from mox.Event import Event
import threading
from random import choice
from config import *
from Notofication_Controller import *

engine = create_engine('sqlite:///hakaton.db')

Session = sessionmaker(bind=engine)
session_db = Session()    

def event_fill(n):
    
    event_arr = [Event().fill(i) for i in range(n)]
    
    for event in event_arr:

        a = e(spending=event.spending, reason=event.reason, date=event.date)
        session_db.add(a)
        session_db.commit()

def ticket_fill(n):
    
    ticket_arr = [Ticket().fill(i) for i in range(n)]
    
    for ticket in ticket_arr:

        a = t(id=ticket.id, price=ticket.spending, race_number=ticket.race_id, date_arrive=ticket.date_arrive, date_comeback=ticket.date_comeback, home=ticket.home, away=ticket.away)
        session_db.add(a)
        session_db.commit()

def random_event():
    if(choice([0, 1])):
        if(choice([0, 1])):
            tick = choice(session_db.query(t).all())
            r_date = tick.date_arrive
            tick.date_arrive = choice(DATES)
            r_n_date = tick.date_arrive
            session_db.commit()
            send_message("npnbem.fm@gmail.com", text_gen("trip_reschedule", "username", tick.race_number, r_date, r_n_date))
  
        else:

            tick = choice(session_db.query(t).all())
            r_date = tick.date_comeback
            tick.date_comeback = choice(DATES)
            r_n_date = tick.date_comeback
            session_db.commit()
            send_message("npnbem.fm@gmail.com", text_gen("trip_reschedule", "username", tick.race_number, r_date, r_n_date))

def timer():
    threading.Timer(5.0, timer).start()
    random_event()

timer()