import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Hello World")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)
