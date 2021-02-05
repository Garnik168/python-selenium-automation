from selenium.webdriver.common.by import By
from behave import given, when, then

CART = (By.ID, 'nav-cart')
CART_TEXT = (By.CSS_SELECTOR, 'div.a-column.a-span8.a-span-last h2')


@when('Click on Cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(*CART).click()


@then('Verify that Cart is Empty')
def verify_cart_is_empty(context):
    actual_result = context.driver.find_element(*CART_TEXT).text
    expected_result = 'Your Amazon Cart is empty'
    assert actual_result == expected_result, f'Expected {expected_result}, got {actual_result} instead'
