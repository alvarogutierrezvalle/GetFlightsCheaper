# This file will need to use the DataManager,FlightSearch, , NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()

city_to_search = input("Which City do you want to search cheaper flight?")

name_city = data_manager.read_data(city_to_search)['city']

lowest_price = data_manager.read_data(city_to_search)['lowestPrice']

try:
    list_data_flight = flight_search.search_flight(name_city, lowest_price)

except:
    print(f"There are not cheapest flight to {city_to_search}")

else:
    new_cost = list_data_flight["cost"]
    data_manager.update_price(city_to_search, new_cost)
    print(list_data_flight)
    print(f"Google Link: https://www.google.com/travel/flights?hl=es#flt={list_data_flight['flyfrom']}.{list_data_flight['flyTo']}.{list_data_flight['departure']}*{list_data_flight['flyTo']}.{list_data_flight['flyfrom']}.{list_data_flight['toReturn']}")
    notification = NotificationManager(list_data_flight['flyfrom'],list_data_flight['cityTo'],list_data_flight['cost'],list_data_flight['departure'],list_data_flight['toReturn'])
