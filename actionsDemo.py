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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver.maximize_window()
action = ActionChains(driver)
#action.double_click(driver.find_element(By.))
#action.click_and_hold()
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform() #perform() is must!!!!
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

