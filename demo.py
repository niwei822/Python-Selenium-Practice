from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.google.com")
element = driver.find_element(By.XPATH, '//*[@name="q"]')
time.sleep(2)
element.clear()
element.send_keys("ChromeDriver")
element.send_keys(Keys.RETURN)
time.sleep(5)

driver.get("http://www.google.com")
element = driver.find_element("link text",'Gmail')
time.sleep(2)
element.click()
time.sleep(5)