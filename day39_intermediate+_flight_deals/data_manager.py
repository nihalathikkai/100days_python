import requests
from pprint import pprint
from env import TOKEN

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_data(self):
        api_url = "https://api.sheety.co/05718e36fb70ee70027b841f529b82c0/flightDeals/prices"
        header = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url=api_url, headers=header)
        response.raise_for_status()
        result = response.json()
        # pprint(result, width=200)
        return result["prices"]
    
    def update_data(self, data:dict):
        api_url = "https://api.sheety.co/05718e36fb70ee70027b841f529b82c0/flightDeals/prices"
        header = {"Authorization": f"Bearer {TOKEN}"}
        id = data["id"]
        body =  {
            "price": {
                # "city" : "",
                "iataCode" : data["iataCode"]
                # "lowestPrice" : 
            }
        }
        response = requests.put(url=f"{api_url}/{id}", headers=header, json=body)
        response.raise_for_status()
        print(response.text)
        
        
# d = DataManager()
# d.get_data()