from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/garnikdadoyan/Desktop/QA Automation/Automation Classes JobEasy/python-selenium-automation/chromedriver')
driver.implicitly_wait(4)

driver.get('https://www.amazon.com/')

orders_button = driver.find_element(By.XPATH, "//a[@id='nav-orders']//span[@class='nav-line-2']")
orders_button.click()

actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
expected_result = "Sign-In"

assert expected_result == actual_result, f'Expected to see {expected_result} page, got {actual_result} instead'

driver.quit()
