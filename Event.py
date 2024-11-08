from config import *
from random import choice

class Event:
    
    def __init__(self, spending=None, date=None, reason=None): # Базовый класс: Event()==None
        self.spending = spending
        self.date = date
        self.reason = reason

    def fill(self): # Заполняет рандомными значениями из файла конфига переменную типа Event: Event().fill()==Заполненный Event
        sp = choice(SPENDINGS)
        d = choice(DATES)
        r = choice(REASONS)
        return Event(sp, d, r)
    
    def all(self): # Функция, возвращающая словарь из всех значений Event'a: Event().fill().all()~~{'spendings': 'asdad', 'date': 'qew', 'reason': 'qew'}
        return {"spendings":self.spending,
                "date":self.date,
                "reason":self.reason}