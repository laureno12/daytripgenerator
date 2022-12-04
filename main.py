list_of_cities = ["New York City", "Boston", "Philadelphia", "Orlando", "Cleveland", "Dallas", "Las Vegas", "Phoenix", "Los Angeles"]
transportation_method = ["car", "bus", "train", "ride share", "walk"]
restaurant_options = [""]
entertainment_options = ["shopping", "movie", "nature walk", "museum", "guided tour"]
import random

random_city = random.choice(list_of_cities)
print(random_city)

random_transport = random.choice(transportation_method)
print(random_transport)

random_entertainment = random.choice(entertainment_options)
print(random_entertainment)