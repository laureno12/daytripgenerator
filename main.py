list_of_cities = ["New York City", "Boston", "Philadelphia", "Orlando", "Cleveland", "Dallas", "Las Vegas", "Phoenix", "Los Angeles"]
transportation_method = ["car", "bus", "train", "ride share", "walk"]
restaurant_options = [""]
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
            print("Awesome!")
            confirm_city = True


random_transport = random.choice(transportation_method)
print(random_transport)

random_entertainment = random.choice(entertainment_options)
print(random_entertainment)