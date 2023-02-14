import requests
from datetime import datetime, timezone
from time import sleep
import smtplib

MY_LAT = 8.524139
MY_LNG = 76.936638

def send_email():
    my_email = "mfreeman287p@gmail.com"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="rsbhslpmkjcktwyn")
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Look Up ⬆\n\nLook up to see ISS passing by...")

def get_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()["iss_position"]
    lat = float(data["latitude"])
    lng = float(data["longitude"])
    return (lat,lng)

def iss_within_range():
    iss_lat, iss_lng = get_iss_location()
    if MY_LAT-5<iss_lat<MY_LAT+5 and MY_LNG-5<iss_lng<MY_LNG+5:
        print("ISS is in range")
        return True
    else:
        print("ISS not in range")
        return False

def get_sunrise_sunset():
    response = requests.get(
        url="https://api.sunrise-sunset.org/json",
        params={
            "lat":MY_LAT,
            "lng":MY_LNG,
            "formatted":0}
    )
    response.raise_for_status()
    data = response.json()["results"]
    sunrise = datetime.strptime(data["sunrise"], "%Y-%m-%dT%H:%M:%S%z")
    sunset = datetime.strptime(data["sunset"], "%Y-%m-%dT%H:%M:%S%z")
    return (sunrise, sunset)

def is_night():
    time_now = datetime.now(tz=timezone.utc)
    sunrise, sunset = get_sunrise_sunset()
    if time_now<sunrise or time_now>sunset:
        print("Night time")
        return True
    else:
        print("Day time")
        return False


while True:
    if iss_within_range() and is_night():
        print("Look Up!")
        send_email()
    sleep(60)