from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

#A000000@a
#cici@gmail.com
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("cici@gmail.com")
driver.find_element(By.ID, "userPassword").send_keys("A000000@a")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("A000000@a")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
time.sleep(2)