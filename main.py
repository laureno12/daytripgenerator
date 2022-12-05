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
            select_city
        else:
            print("Awesome! Let's move on!")
            confirm_city = True
    
select_city (list_of_cities)


def select_transport (transportation_method):
    confirm_transport = False
    while confirm_transport == False:
        select_transport = random.choice(transportation_method)
        user_input = input (f"You'll be transported by {select_transport}! Do you accept? (y/n) ")
        if user_input == "n":
            print("No worries! Let's try again!")
            select_transport
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
            select_restaurant
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
            select_entertainment
        else:
            print("Awesome! Let's move on!")
            confirm_entertainment = True
    
select_entertainment (entertainment_options)





