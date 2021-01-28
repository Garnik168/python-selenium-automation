from selenium.webdriver.common.by import By
from behave import given, then


@given('Open Amazon main page')
def open_amazon_main_page(context):
    context.driver.get('https://www.amazon.com/')


@then('Click on Orders')
def locate_and_click_on_orders_button(context):
    orders_button = context.driver.find_element(By.XPATH, "//a[@id='nav-orders']//span[@class='nav-line-2']")
    orders_button.click()


@then('User is taken to Sign in page')
def verify_user_is_on_sign_in_page(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    expected_result = "Sign-In"
    assert expected_result == actual_result, f'Expected to see {expected_result} page, got {actual_result} instead'

