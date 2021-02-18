import requests
from tohide import InfoHiden

TOKEN = InfoHiden["NT_TOKEN"]
PRICE_SHEET_ENDPOINT = InfoHiden["NT_SHEET"]
BEARER = {
    "Authorization": f"Bearer {TOKEN}"
}


class DataManager:

    def read_data(self, city):
        response = requests.get(url=PRICE_SHEET_ENDPOINT, headers=BEARER)
        response.raise_for_status()
        data = response.json()
        for city_params in data['prices']:
            if city_params['city'] == city:
                return city_params

    def update_price(self, city, new_price):
        new_url = f"{PRICE_SHEET_ENDPOINT}/{self.read_data(city)['id']}"
        lowest_price = self.read_data(city)['lowestPrice']
        if new_price < lowest_price:
            price_uploaded = [new_price, lowest_price]
            data_params = {
                'price':
                    {
                        'lowestPrice': price_uploaded[0],
                        'oldPrice': price_uploaded[1],
                    }
            }
            response = requests.put(url=new_url, json=data_params, headers=BEARER)
            return response.raise_for_status()
        else:
            return "No Changes"
