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
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Click Here").click()
#driver.window_handles ->list of opened windows
driver.switch_to.window(driver.window_handles[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
driver.switch_to.window(driver.window_handles[1])
email = driver.find_element(By.XPATH, "//p//strong//a").text
print(email)
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
message = driver.find_element(By.CLASS_NAME, "alert").text
print(message)
#.alert strong
