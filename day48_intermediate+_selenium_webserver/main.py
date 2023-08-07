from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(service=service, options=options)

# driver.get("https://www.amazon.com")

# driver.get("https://amzn.eu/d/5ust5R8")
# element = driver.find_elements(By.CLASS_NAME, "a-price-whole")
# element = driver.find_elements(By.CLASS_NAME, "a-offscreen")
# element = driver.find_elements(By.CSS_SELECTOR, ".priceToPay .a-price-whole")
# element = driver.find_elements(
# By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
# print(element)
# for _ in element:
#     print(_.get_attribute("innerHTML"))


# driver.get("https://www.amazon.com")
# # element = driver.find_elements(By.ID, "twotabsearchtextbox")
# element = driver.find_elements(By.NAME, "field-keywords")
# for _ in element:
#     print(_.get_attribute("placeholder"))


driver.get("https://www.python.org/")
element = driver.find_element(
    By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
elements = element.find_elements(By.TAG_NAME, 'li')
for _ in elements:
    print(_.get_attribute("innerHTML"))


# driver.close()
driver.quit()
