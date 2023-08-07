import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(name="h3", class_="title")

# for _ in titles: print(_.getText())

title_list = [_.getText() for _ in titles][::-1]

# for _ in title_list: print(_)


with open(file="D:\\python\\100days\\day45_intermediate+_beautifulsoup\\movies.txt", 
          mode="w",
          encoding="utf-8") as file:
    file.write('\n'.join(title_list))
        
print("Done")