from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time

driver = webdriver.Chrome()
driver.get("http://www.facebook.com")
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys("qiqi7722@hotmail.com")
pw = driver.find_element(By.XPATH, '//*[@id="pass"]')
pw.send_keys("Test@123")

submit = driver.find_element(By.NAME, 'login')
submit.click()
time.sleep(5)

status = driver.find_element(By.LINK_TEXT,"What's on your mind, Gong?")
status.click()
time.sleep(5)