import time
from selenium import webdriver
#chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#--Chrome Browser
service_obj = Service("O:\QA\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
login = driver.find_element(By.CSS_SELECTOR, ".ui-url").text #your web page is broken that's why this way
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID, "username").send_keys(login)
driver.find_element(By.ID, "password").send_keys("examplePass")
driver.find_element(By.ID, "signInBtn").click()
time.sleep(3)
assert "Incorrect username/password." == driver.find_element(By.CSS_SELECTOR, ".alert").text