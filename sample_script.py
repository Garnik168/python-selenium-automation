from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/garnikdadoyan/Desktop/QA Automation/Automation Classes JobEasy/python-selenium-automation/chromedriver')
driver.implicitly_wait(10)      # checks every 100 ms (1/10 of a second)
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# # wait for 4 sec
driver.wait = WebDriverWait(driver, 10)
e = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))  # 500ms (1/2 of a second)

# click search
e.click()

# verify
assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text

driver.quit()
