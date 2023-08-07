from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\Development\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.python.org/")
# element = driver.find_element(
#     By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]')
element = driver.find_element(By.CSS_SELECTOR, ".event-widget .menu")
list_items = element.find_elements(By.TAG_NAME, "li")


data = dict()

for i, list_item in enumerate(list_items):
    # print(list_item.text)
    datetime = list_item.find_element(
        By.TAG_NAME, "time").get_attribute("datetime")
    date = datetime.split('T')[0]
    text = list_item.find_element(By.TAG_NAME, 'a').text
    data[i] = {'time': date, 'name': text}

print(data)

driver.quit()
