from bs4 import BeautifulSoup

with open("D:/python/100days/day45_intermediate+_beautifulsoup/website.html", encoding="utf8") as file:
    contents = file.read()
    
# print(contents)
soup = BeautifulSoup(contents, 'html.parser')

# print(soup.prettify())

all_anchor_tags = soup.find_all(name='a')

print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    
for tag in all_anchor_tags:
    print(tag.get("href"))
    
    
heading = soup.find(name="h1", id='name')
print(heading)

section_heading = soup.find(class_="heading")
print(section_heading)

section_heading = soup.find_all(class_="heading")
print(section_heading)

company_url = soup.select_one(selector="body p")
print(company_url)

company_url = soup.select(selector="body p")
print(company_url)

print(soup.a)