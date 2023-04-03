#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import smtplib

from data_manager import DataManager
from flight_search import FlightSearch
    
def send_mail(to_address, message):
    my_email = "mfreeman287p@gmail.com"
    password = "rsbhslpmkjcktwyn"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=message)
        
        
data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_data()
# pprint(sheet_data)

for loc in sheet_data:
    if not loc["iataCode"]:
        loc["iataCode"] = flight_search.search_iata_code(loc["city"])
        data_manager.update_data(loc)
        
# pprint(sheet_data)

for destination in sheet_data:
    city = destination["city"]
    iata_code = destination["iataCode"]
    flight_data = flight_search.search_flicht_cost("LON", iata_code)
    # print(f"{city} : {flight_data.price}; {destination['lowestPrice']}")
    if flight_data.price <= destination["lowestPrice"]:
        message = f"Subject:Flight Deal Alert ({flight_data.cityFrom}-{flight_data.cityTo})!!!\n\nOnly {flight_data.price} GBP to fly from {flight_data.cityFrom}-{flight_data.flyFrom} to {flight_data.cityTo}-{flight_data.flyTo}, from {flight_data.local_arrival} to {flight_data.local_departure}"
        
        send_mail(to_address="mfreeman287p@gmail.com", message=message)
        
    

        
        
