import sys
import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Drink
from db.models import Order
from db.models import Customer 

if __name__ == '__main__':

    engine = create_engine('sqlite:///db/drinks.db')
    Session = sessionmaker(bind=engine)
    session = Session() 
    ipdb.set_trace()