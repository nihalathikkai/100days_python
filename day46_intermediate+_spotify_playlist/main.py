import requests
from bs4 import BeautifulSoup

date = input("Enter year in  YYY-MM-DD format: ")

url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')

songs_list = soup.select("body div main div div div div div div div ul li ul li h3")
artists_list = soup.select("body div main div div div div div div div ul li ul li span.a-no-trucate")

songs = [_.getText().strip() for _ in songs_list]
artists = [_.getText().strip() for _ in artists_list]

data = [(song, artist) for song, artist in zip(songs, artists)]

for _ in data: print(_)

# print(songs)
# print(artists)





# 2b79eef4bc9443d78888e35fdcab66a4

# 678fefba58954e968ab9fcd66202acb6


