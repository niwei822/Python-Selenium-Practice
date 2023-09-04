from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

#click the header
driver.find_element(By.XPATH, "//span[.='Veg/fruit name']").click()
results = driver.find_elements(By.XPATH, "//tr/td[1]")
sort_list = []
for result in results:
    sort_list.append(result.text)
original_list = sort_list.copy()
sort_list.sort()
assert original_list == sort_list
