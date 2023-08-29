from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.google.com")
element = driver.find_element("name", "q")
time.sleep(2)
element.clear()
element.send_keys("ChromeDriver")
element.send_keys(Keys.RETURN)
time.sleep(5)