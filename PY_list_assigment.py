import time

from selenium import webdriver
#chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#--Chrome Browser
service_obj = Service("O:\QA\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2) #global time-out, max time-out. Wait for a element
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2) #without it there will be an empty list in results list[]
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)   #append дописывать данные в лист

print(actualList)
assert actualList == expectedList





