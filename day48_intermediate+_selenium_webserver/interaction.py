from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\Development\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(service=service, options=options)

driver

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)
driver.fullscreen_window()

article_count = driver.find_element(By.CSS_SELECTOR, "div#articlecount a")
# print(article_count.get_attribute("innerHTML"))
print(article_count.text)
# article_count.click()

content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# content_portals.click()

# search_bar = driver.find_element(By.CLASS_NAME, "cdx-text-input__input")
search_bar = driver.find_element(By.NAME, "search")
# search_bar = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div/div[1]/input//*[@id="searchform"]/div/div/div[1]/input')
search_bar.send_keys("Python")
# print(search_bar.get_attribute("placeholder"))


sleep(5)
driver.quit()
