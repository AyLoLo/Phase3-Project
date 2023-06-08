import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Drink
from db.models import Order
from db.models import Customer 

if __name__ == '__main__':

    engine = create_engine('sqlite:///db/drinks.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Ayooo Boss, Welcome To Our Tipsy Fam Bar!")
    print("What can I get for you today?")
    user_input = input('Enter "c" to create a new drink\nEnter "r" to get a list of our drinks\nEnter "u" to update existing drinks\nEnter "d" to delete drinks\nEnter "p" to see a list of our previous orders\nEnter "o" to create an order\nEnter "m" if you want to close the bar and clear all orders\n')

    while(not user_input in ['c', 'r', 'u', 'd', 'p', 'o', 'm']):
        print("Sorry amigo, I didn't quite catch that. ")
        user_input = input('Enter "c" to create a new drink\nEnter "r" to get a list of our drinks\nEnter "u" to update existing drinks\nEnter "d" to delete drinks\nEnter "p" to see a list of our previous orders\nEnter "o" to create an order\nEnter "m" if you want to close the bar and clear all orders\n')

    if user_input == 'c':
        print("Aye, what's this hot new drink? ")
        drink_name = input("Tell me what's the name of your hot new drink:\n")
        drink = Drink(name = drink_name)
        
        session.add(drink)
        session.commit()
        
        print(f"Sheesh! Your hot new drink, {drink.name}, is on the shelf!")

    if user_input == 'o':
        print("So you wanted to place an order, eh?")
        
        drinks = session.query(Drink).all()
        customers = session.query(Customer).all()

        drink_id_order = int(input("What drink number(id) would you like? "))
        if 0 < drink_id_order <= len(drinks):
            print("Dass a good drink!")
        else:
             raise Exception("Must be a valid ID for an existing drink!")
        
        order_amount = input("How many of that? Just one? Two? How many? ")
        
        customer_id_order = int(input("And this is for which customer(id) ...? "))
        if 0 < customer_id_order <= len(customers):
            print("You got it boss!")
        else:
            raise Exception("Must be a valid ID for an existing customer!")

        customer_order = Order(drink_id = drink_id_order, times_ordered = order_amount, customer_id = customer_id_order)
        session.add(customer_order)
        session.commit()

        print(f"Gotcha, your order has been noted!")
    
    elif user_input == 'r':
        print("Sure fam, I can tell you all about these drinks!")
        drinks = session.query(Drink)
        
        print(f"These are our {drinks.count()} drinks available!")
        print("Here is the business with all of our drinks:")
        for drink in drinks:
            print(f"Drink #{drink.id} : {drink.name}")
    
    elif user_input == 'p':
        print("Amigo, I could tell you what others before have ordered!")
        print("Here's a list of our customers kryptonites")
        
        orders = session.query(Order).all()
        for order in orders:
            print(order)
    

    elif user_input == 'u':
        print("I heard you wanted to change up our drinks!")
        drinks = session.query(Drink)
        print("Here is the business with all of our drinks: ")
        for drink in drinks:
            print(f"Drink #{drink.id} : {drink.name}")
        
        drink_id = input("Tell me the digits for the id of the drink you want to shake up: ")
        drink = drinks.filter(Drink.id == int(drink_id)).first()
        drink_name = input("Tell me, what's the new name for this sweet goddess of a drink?: ")
        drink.name = drink_name
        
        session.commit()
        print(f"Sheesh! I like this new name, {drink.name}, for Drink #{drink.id}!")

    elif user_input == 'd':
        print("Whoa, I heard the drinks were not vibing well! ")
        drinks = session.query(Drink)
        
        print("Here is the business with all of our drinks: ")
        for drink in drinks:
            print(f"Drink #{drink.id} : {drink.name}")
        
        drink_id = input("Amigo, tell me, which specific drink number needs to get knocked off or just say 'Tipsay' to knock out all drinks: ")
        if drink_id == 'Tipsay':
            drinks.delete()
            session.commit()
            print("Great! I no longer have a business!")
        else:  
            drink = drinks.filter(Drink.id == int(drink_id)).first()
            session.delete(drink)
            session.commit()
            print(f"Say No More! The Drink #{drink.id}: {drink.name} went down the drain!")
    
    elif user_input == 'm':
        print("You want to close up the bar for the day? ")
        orders = session.query(Order)

        clear_orders_input = input("Amigo, say 'Ciao' and we can go home early today! ")
        if clear_orders_input == 'Ciao':
            orders.delete()
            session.commit()
            print("Bueno! We cleaned out for the day! ")
        else:
            print("Ahhh, you are pulling my leg! Time to work overtime! ")
