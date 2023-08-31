from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.google.com")
print(driver.title)
element = driver.find_element(By.XPATH, '//*[@name="q"]')
time.sleep(2)
element.clear()
element.send_keys("ChromeDriver")
#simulates pressing the "Enter" key, which triggers the search action.
element.send_keys(Keys.RETURN)
time.sleep(5)

driver.get("http://www.google.com")
element = driver.find_element("link text",'Gmail')
time.sleep(2)
element.click()
time.sleep(5)
print(driver.current_url)
#refresh page
driver.get("http://www.google.com")
time.sleep(5)
driver.refresh()

driver.get("http://www.google.com")
element = driver.find_element("link text",'Gmail')
time.sleep(2)
element.click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/")
ele = driver.find_element("tag name", "html")
ele.send_keys(Keys.END)
time.sleep(5)
ele.send_keys(Keys.HOME)
time.sleep(5)