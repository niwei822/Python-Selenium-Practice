from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from time import sleep

#//tagname[@atribute='value']
#css_selector = tagname[atribute='value']
# #id

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
name = driver.find_element(By.NAME, "name")

name.send_keys("cici")
time.sleep(2)
email = driver.find_element(By.XPATH, "//input[@name='email']")
email.send_keys("cici@gmail")
time.sleep(2)
pw = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
pw.clear()
pw.send_keys("12345")
time.sleep(2)

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

status = driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio1']")
status.click()
time.sleep(2)

submit = driver.find_element(By.XPATH, "//input[@value='Submit']")
submit.click()
time.sleep(2)
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

binding = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
binding.clear()
binding.send_keys("hello")

time.sleep(2)
