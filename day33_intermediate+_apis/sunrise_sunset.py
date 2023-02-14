import requests
from datetime import datetime
from dateutil import tz


def convert_to_datetime(time):
    utc_time =  datetime.strptime(time, "%Y-%m-%dT%H:%M:%S%z")
    # utc_time =  utc_time.replace(tzinfo=tz.tzutc())
    local_time = utc_time.astimezone(tz=tz.tzlocal())
    return local_time

url = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat":8.524139, 
    "lng":76.936638,
    "formatted": 0
    }


response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()["results"]

sunrise = convert_to_datetime(data["sunrise"])
sunset = convert_to_datetime(data["sunset"])
print(sunrise, sunset)

now = datetime.now()
print(now)