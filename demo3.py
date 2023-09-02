from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for i in checkboxes:
    if i.get_attribute("value") == "option2":
        i.click()
        i.is_selected()
        break
time.sleep(2)

radios = driver.find_elements(By.XPATH, "//input[@type='radio']")
for radio in radios:
    if radio.get_attribute("value") == "radio1":
        radio.click()
        assert radio.is_selected()
        break
time.sleep(2)

assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()
time.sleep(2)
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
name = "cici"
driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
print(alert.text)
assert name in alert.text
#click on ok
alert.accept()
#click on cancel
#alert.dismiss()
