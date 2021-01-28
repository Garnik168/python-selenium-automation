from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/garnikdadoyan/Desktop/QA Automation/Automation Classes JobEasy/python-selenium-automation/chromedriver')
driver.implicitly_wait(4)


driver.get('https://www.amazon.com/')

search_field = driver.find_element(By.ID, 'twotabsearchtextbox')
search_field.send_keys('Lightsaber')

search_icon_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_icon_button.click()

actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
expected_text = '"Lightsaber"'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text} instead'

driver.quit()

