from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

m = MetaData(naming_convention=convention)

Base = declarative_base(metadata=m)

class Drink(Base):
    __tablename__ = 'drinks'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    orders = relationship('Order', backref='drink')
    customers = association_proxy("orders", "customer",
        creator=lambda c: Order(customer=c))


    def __repr__(self):
        return f"Drink #{self.id}: {self.name}"
    
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    name = first_name + last_name

    orders = relationship("Order", backref="customer")
    drinks = association_proxy("orders", "drink",
        creator=lambda d: Order(drink=d))

    def __repr__(self):
        return f"Customer #{self.id}: {self.first_name} {self.last_name}"
    
class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer(), primary_key=True)
    times_ordered = Column(String())
    
    drink_id = Column(Integer(), ForeignKey('drinks.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    def __repr__(self):
        return f"{self.customer.first_name} ordered {self.drink.name} {self.times_ordered} time(s)"
