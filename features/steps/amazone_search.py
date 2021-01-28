from selenium.webdriver.common.by import By
from behave import given, when, then



@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input Lightsaber into Amazon search field')
def input_amazon_search(context):
    search_field = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_field.send_keys('Lightsaber')


@when('Click on Amazon search icon')
def click_amazon_search_icon(context):
    search_icon_button = context.driver.find_element(By.ID, 'nav-search-submit-button')
    search_icon_button.click()


@then('Product results for Lightsaber are shown on Amazon')
def product_results_are_shown(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    expected_text = '"Lightsaber"'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text} instead'



