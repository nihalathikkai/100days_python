import requests
from pprint import pprint
from datetime import datetime, timedelta

from flight_data import FlightData

from env import API_KEY
API_URL = "https://api.tequila.kiwi.com"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def search_iata_code(self, city: str):
        # print(f"Searching city code for {city}")
        api_url = f"{API_URL}/locations/query"
        header = {
            "apikey" : API_KEY
        }
        parameters = {
            "term" : city,
            "locale" : "en-US",
            "location_types" : "airport",
            "limit": 1,
            "active_only" : True
        }
        response = requests.get(url = api_url, headers=header, params=parameters)
        
        response.raise_for_status()
        result = response.json()
        code = result["locations"][0]["city"]["code"]
        return code
    
    def search_flicht_cost(self, fly_from, fly_to):
        api_url = f"{API_URL}/v2/search"
        header = {
            "apikey" : API_KEY
        }
        now = datetime.now()
        parameters = {
            "fly_from" : fly_from,
            "fly_to": fly_to,
            "date_from" : now.strftime("%d/%m/%Y"),
            "date_to " : (now+timedelta(days=6*30)).strftime("%d/%m/%Y"),
            "nights_in_dst_from" : 7,
            "nights_in_dst_to" : 28,
            "flight_type" : "round",
            "curr" : "GBP",
            "one_for_city" : 1,
            "max_stopovers" : 0            
        }
        
        response = requests.get(url = api_url, headers=header, params=parameters)
        response.raise_for_status()
        result = response.json()
        # print(result)
        data = result["data"][0]
        flight_data = FlightData(
            price = data["price"],
            flyFrom = data["flyFrom"],
            flyTo = data["flyTo"], 
            cityFrom = data["cityFrom"], 
            cityTo = data["cityTo"], 
            local_arrival = data["local_arrival"].split('T')[0], 
            local_departure = data["local_departure"].split('T')[0]
        )
        return flight_data
        

# f = FlightSearch()
# print(f.search_iata_code("Paris"))
# print(f.search_flicht_cost("LON", "PAR"))