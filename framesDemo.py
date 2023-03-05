import time

from selenium import webdriver
from selenium.webdriver import ActionChains
#chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#--Chrome Browser
service_obj = Service("O:\QA\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2) #global time-out, max time-out. Wait for a element
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(2)

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)






