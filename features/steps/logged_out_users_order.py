from selenium.webdriver.common.by import By
# same thing here, should I remove the above import of By?
from behave import given, then


@given('Open Amazon main page')
def open_amazon_main_page(context):
    context.app.main_page.open_main_page()


@then('Click on Orders')
def locate_and_click_on_orders_button(context):
    context.app.main_page.click_orders_button()


@then('User is taken to Sign in page')
def verify_user_is_on_sign_in_page(context):
    context.app.sign_in_page.verify_user_is_on_sign_in_page()


