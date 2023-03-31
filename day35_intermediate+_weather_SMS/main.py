import requests
import smtplib
from env import API_KEY

def send_mail():
    email = "mfreeman287p@gmail.com"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password="rsbhslpmkjcktwyn")
        connection.sendmail(from_addr=email, to_addrs=email, msg="Subject:Rain Forecast\n\nBring an Umbrella")
    
def get_lat_lon(city):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    parameters = {
        "q": city,
        "limit":5,
        "appid": API_KEY
    }
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    data = response.json()[0]
    return data["lat"], data["lon"]


def get_current_weather(lat,lon):
    url = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY
    }
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    return response.json()


def get_weather_forecast(lat,lon):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    parameters = {
        "lat": lat,
        "lon": lon,
        "units": "metric",
        "cnt": 4,
        "appid": API_KEY
    }
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    return response.json()
    
    
def need_umbrella(lat,lon):
    data = get_weather_forecast(lat,lon)
    for forecast in data["list"]:
        code = forecast["weather"][0]["id"]
        # print(code)
        if code < 700:
            print("Bring umbrella")
            send_mail()
            break
    
    
city = "Clarksville"#"Trivandrum"
lat, lon = get_lat_lon(city)
print(lat, lon) 
# get_current_weather(lat,lon)
# onecall(lat,lon)
# get_weather_forecast(lat,lon)
need_umbrella(lat,lon)