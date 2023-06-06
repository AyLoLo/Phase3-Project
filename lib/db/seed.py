from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Drink
from models import Customer
from models import Order

if __name__ == '__main__':

    engine = create_engine("sqlite:///drinks.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    drink1= Drink(name="Perfect Pear")
    drink2 = Drink(name="The Holy Father")
    drink3 = Drink(name="Phoenix Down")
    drink4 = Drink(name="Lost And Found")
    drink5 = Drink(name="Midnight Moon")
    drink6 = Drink(name="Stardust Spritz")
    drink7 = Drink(name="A Shot Of Shadow Mezcal")

    customer1 = Customer(first_name="Eylem", last_name="Aytas")
    customer2 = Customer(first_name="Anthony", last_name="Lopez")
    customer3 = Customer(first_name="Claire", last_name="Mccafferty")
    customer4 = Customer(first_name="Ricardo", last_name="Guerra")

    order1 = Order(times_ordered=2, drink_id=2, customer_id=1)
    order2 = Order(times_ordered=2, drink_id=3, customer_id=2)
    order3 = Order(times_ordered=1, drink_id=1, customer_id=3)
    order4 = Order(times_ordered=1, drink_id=2, customer_id=3)
    order5 = Order(times_ordered=1, drink_id=3, customer_id=3)
    order6 = Order(times_ordered=1, drink_id=4, customer_id=3)
    order7 = Order(times_ordered=1, drink_id=5, customer_id=3)
    order8 = Order(times_ordered=1, drink_id=6, customer_id=3)
    order9 = Order(times_ordered=1, drink_id=7, customer_id=3)
    order10 = Order(times_ordered=2, drink_id=5, customer_id=1)
    order11 = Order(times_ordered=10, drink_id=2, customer_id=4)
    order12 = Order(times_ordered=1, drink_id=7, customer_id=1)
    order13 = Order(times_ordered=1, drink_id=7, customer_id=2)
    order14 = Order(times_ordered=1, drink_id=7, customer_id=3)
    order15 = Order(times_ordered=1, drink_id=7, customer_id=4)

    session.add_all([drink1, drink2, drink3, drink4, drink5, drink6, drink7, customer1, customer2, customer3, customer4, order1, order2, order3, order4, order5, order6, order7, order8, order9, order10, order11, order12, order13, order14, order15])
    session.commit()