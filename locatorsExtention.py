from selenium import webdriver
#chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#--Chrome Browser
service_obj = Service("O:\QA\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com") #a path for Xpath with "/"
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("123456") #a path for CSS with "space"
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("123456")
#driver.find_element(By.XPATH, "//button[@type='submit']").click() # 1st option
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click() #2nd option
#input()

