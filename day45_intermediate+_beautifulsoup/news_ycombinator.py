import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(name="span", class_="titleline")
score = soup.find_all(name="span", class_="score")

titles = soup.select(".titleline")
scores = soup.select(".score")


# for title,score in zip(titles, scores):
#     print(title.a.getText())
#     print(title.a.get('href'))
#     print(score.getText().split()[0])
#     print("__________________________________________________")


data = [(title.a.getText(), title.a.get('href'), int(score.getText().split()[0])) for title,score in zip(titles, scores)]

# for _ in data: print(_)

# sorted_data = sorted(data, key=lambda x: x[2], reverse=True)
# for _ in sorted_data: print(_)

data.sort(key=lambda x: x[2], reverse=True)
for _ in data: print(_)