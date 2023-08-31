from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

#//tagname[@atribute='value']
#css_selector = tagname[atribute='value']

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
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
status = driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio1']")
status.click()
time.sleep(2)

