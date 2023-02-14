import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# print(response)
# print(response.headers)
# print(response.content)

data = response.json()

print(data)
iss_position = (data['iss_position']['latitude'], data['iss_position']['longitude'])

print(iss_position)

response.raise_for_status()