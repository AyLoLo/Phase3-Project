import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Drink

if __name__ == '__main__':

    engine = create_engine('sqlite:///db/drinks.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Ayooo Tipsy Fam, Welcome To Our Bar!")
    print("What can I get for you today?")
    user_input = input('Enter "c" to create a new drink\nEnter "r" to get / read info about drinks\nEnter "u" to update existing drinks\nEnter "d" to delete drinks\n')

    while(not user_input in ['c', 'r', 'u', 'd']):
        print("Say what? No comprende")
        print("Please, today, what would you like?")
        user_input = input('Enter "c" to create a new drink\nEnter "r" to get / read info about drinks\nEnter "u" to update existing drinks\nEnter "d" to delete drinks\n')

    if user_input == 'c':
        print("Aye, what's this hot new drink?")
        drink_name = input("Tell me what's the name of your hot new drink:\n")
        drink = Drink(name = drink_name)
        session.add(drink)
        session.commit()
        
        print(f"Sheesh! Your hot new drink, {drink.name}, is on the shelf!")
    
    elif user_input == 'r':
        print("Sure fam, I can tell you all about these drinks!")
        drinks = session.query(Drink)
        print(f"These are all of our {drinks.count()} drinks available!")
        print("Here is the business with all of our drinks:")
        for drink in drinks:
            print(drink)

    elif user_input == 'u':
        print("I heard you wanted to change up our drinks!")
        drinks = session.query(Drink)
        print("Here is the business with all of our drinks: ")
        for drink in drinks:
            print(drink)
        drink_id = input("Tell me the digits for the id of the drink you want to shake up: ")
        drink = drinks.filter(Drink.id == int(drink.id)).first()
        drink_name = input("Tell me, what's the new name for this sweet goddess of a drink?: ")
        drink.name = drink_name
        session.commit()
        print(f"Sheesh! I like this new name, {drink.name}, for Drink #{drink.id}!")

    elif user_input == 'd':
        print("Whoa, you want to get rid of ALL of our drinks?")
        drinks = session.query(Drink)
        print("Here is the business with all of our drinks: ")
        for drink in drinks:
            print(drink)
        drink_id = input("Compadre, tell me, which specific drink needs to get knocked off or just say 'Tipsay' to get knock out all drinks: ")
        if drink_id == 'Tipsay':
            drinks.delete()
            session.commit()
            print("Great! I no longer have a business!")
        else:
            drink = drinks.filter(Drink.id == int(drink_id)).first()
            session.delete(drink)
            session.commit
            print(f"Say No More! This Drink #{drink.id}: {drink.name} went down the drain!")
