list_of_cities = ["New York City", "Boston", "Philadelphia", "Orlando", "Cleveland", "Dallas", "Las Vegas", "Phoenix", "Los Angeles"]
transportation_method = ["car", "bus", "train", "ride share", "walking"]
restaurant_options = ["Local Diner", "Hot dog stand", "Hotel Bar", "McDonald's"]
entertainment_options = ["shopping", "movie", "nature walk", "museum", "guided tour"]
import random

def select_city (list_of_cities):
    confirm_city = False
    while confirm_city == False:
        select_city = random.choice(list_of_cities)
        user_input = input (f"You're going to {select_city}! Do you accept? (y/n) ")
        if user_input == "n":
            print("No worries! Let's try again!")    
        else:
            print("Awesome! Let's move on!")
            confirm_city = True
            return select_city
        
select_city (list_of_cities)


def select_transport (transportation_method):
    confirm_transport = False
    while confirm_transport == False:
        select_transport = random.choice(transportation_method)
        user_input = input (f"You'll be transported by {select_transport}! Do you accept? (y/n) ")
        if user_input == "n":
            print("No worries! Let's try again!")
        else:
            print("Awesome! Let's move on!")
            confirm_transport = True

select_transport (transportation_method)


def select_restaurant (restaurant_options):
    confirm_restaurant = False
    while confirm_restaurant == False:
        select_restaurant = random.choice(restaurant_options)
        user_input = input (f"You'll eat at {select_restaurant}! Do you accept? (y/n) ")
        if user_input == "n":
            print("No worries! Let's try again!")
        else:
            print("Awesome! Let's move on!")
            confirm_restaurant = True
    
select_restaurant (restaurant_options)

def select_entertainment (entertainment_options):
    confirm_entertainment = False
    while confirm_entertainment == False:
        select_entertainment = random.choice(entertainment_options)
        user_input = input (f"You'll spend some time {select_entertainment}! Do you accept? (y/n) ")
        if user_input == "n":
            print("No worries! Let's try again!")
        else:
            print("Awesome! Let's move on!")
            confirm_entertainment = True
    
select_entertainment (entertainment_options)

print("Looks like we are almost done here. Let's confirm the details of your trip!")

def confirm_trip():
    confirm_trip = False
    while confirm_trip == False:
        user_input = input("Are you ready to book your trip? (y/n) ")
        if user_input == "n":
            print ("Let's start over")
            select_city
            select_transport
            select_entertainment
            select_restaurant
        else:
            print ("Great! Time to start packing!")
            confirm_trip = True
        

confirm_trip()








