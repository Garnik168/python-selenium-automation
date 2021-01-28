from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/Users/garnikdadoyan/Desktop/QA Automation/Automation Classes JobEasy/python-selenium-automation/chromedriver')
driver.implicitly_wait(4)


driver.get('https://www.amazon.com/gp/help/customer/display.html')

help_search_field = driver.find_element(By.ID, 'helpsearch')
help_search_field.send_keys("Cancel order" + Keys.ENTER)

actual_text = driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
# actual_text = driver.find_element(By.XPATH, "//div[@class='a-box-inner']//h1[text()='Cancel Items or Orders']").text
expected_text = 'Cancel Items or Orders'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text} instead'

driver.quit()
