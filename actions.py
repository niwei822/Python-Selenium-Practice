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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
