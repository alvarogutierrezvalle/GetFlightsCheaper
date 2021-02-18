import requests
from datetime import datetime
from datetime import timedelta
from tohide import InfoHiden
API_KEY = InfoHiden["NT_API_KEY"]
KIWI_ENDPOINT = "https://tequila-api.kiwi.com"
HEADERS = {
    'apikey': API_KEY
}

FROM = 'AGP'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_iata(self, city):
        iata_endpoint = KIWI_ENDPOINT + "/locations/query/"
        flight_params = {
            'term': city,
            'locale': "en-US",
            'location_type': "airport",
            'limit': 4
        }
        response = requests.get(url=iata_endpoint, params=flight_params, headers=HEADERS)
        response.raise_for_status()
        data_flight = response.json()
        return data_flight['locations'][0]['code']

    def search_flight(self,city_to_go,lowest):
        search_endpoint = KIWI_ENDPOINT + "/v2/search"
        date_from = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        date_to = (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y")
        code_iata_togo = self.get_iata(city_to_go)
        search_params = {
            "fly_from": FROM,
            "fly_to": code_iata_togo,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 3,
            "flight_type": 'round',
            'adults': 1,
            "selected_cabins": 'M',
            "adult_hold_bag": 0,
            'adult_hand_bag': 1,
            "price_to": lowest,
            "max_sector_stopovers": 2,
            "vehicle_type": "aircraft"
        }
        response = requests.get(url=search_endpoint, params=search_params, headers=HEADERS)
        response.raise_for_status()
        resume = response.json()["data"][0]

        dict_data = {
            "flyTo": resume["flyTo"],
            "cost" : resume["price"],
            "departure" : resume["local_departure"].split("T")[0],
            "toReturn" : resume["route"][-1]["local_departure"].split("T")[0],
            "stopovers" : len(resume["route"]) / 2,
            "nights" : resume["nightsInDest"],
            "flyfrom" : resume["flyFrom"],
            "cityTo" : resume["cityTo"],
            "link" : resume["deep_link"]

        }

        return dict_data



