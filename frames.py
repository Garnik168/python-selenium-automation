from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path='/Users/garnikdadoyan/Desktop/QA Automation/Automation Classes JobEasy/python-selenium-automation/chromedriver')
driver.implicitly_wait(5)


# open url
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe')

# switch to frame 1
driver.switch_to.frame('iframeResult')      # to switch to this element just provide the ID without By

# switch to frame 2
frame_2 = driver.find_element(By.CSS_SELECTOR, "iframe[src='https://www.w3schools.com']")      # cuz element has no ID, we need to find it
driver.switch_to.frame(frame_2)             # providing the element that we found earlier (line above) so it can switch

# verify logo
logo = driver.find_element(By.CSS_SELECTOR, 'a.w3schools-logo')
actual_logo_att = logo.get_attribute('href')
# print(actual_logo_att)       # checking
expected_logo_att = 'https://www.w3schools.com/'

assert actual_logo_att == expected_logo_att, f'Expected {expected_logo_att}, but got {actual_logo_att} instead'

driver.quit()
