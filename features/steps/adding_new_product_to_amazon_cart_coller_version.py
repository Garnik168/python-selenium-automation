from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

# I took a liberty of removing all the locators since they are in the Page object files, is that ok?


@when('Input {search_query} into Amazon search field and hit ENTER')
def input_query_and_hit_enter(context, search_query):
    context.app.main_page.input_query_and_hit_enter(search_query)


@when('Click on the first unsponsored result')
def click_on_first_unsponsored_result(context):
    context.app.search_results_page.click_on_first_unsponsored_result()


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.app.product_page.click_add_to_cart()


@when('Choose No Thanks option for Add ons')
def no_thanks_add_on_option(context):
    context.app.product_page.no_thanks_add_on_option()
    # sleep(1)    # new locator fixes the issue no need for sleep, YAY!


@then('Verify that alert {text} is present')
def verify_add_to_cart_alert(context, text):
    context.app.product_page.verify_add_to_cart_alert(text)


@when('Click on Cart button on the pop-up screen')
def click_on_cart_btn_pop_up(context):
    context.app.product_page.click_on_cart_btn_pop_up()


@then('Verify that there is one item in the cart')
def verify_items_in_cart(context):
    context.app.cart_page.verify_items_in_cart()


@when('Click on Delete button under item in the cart')
def click_delete_button_for_item(context):
    context.app.cart_page.click_delete_button_for_item()


# Locators that are used for the steps that are in other .py files:
#
#
# ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
# CHECKOUT_CART_CONFIRMATION = (By.ID, 'sc-subtotal-label-buybox')
# CART_TEXT = (By.CSS_SELECTOR, 'div.a-column.a-span8.a-span-last h2')
#
#
# Steps, that are defined in other .py files:
#
#
# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')
#
#
# @when('Click on Add to Cart button')
# def click_add_to_cart(context):
#     context.driver.find_element(*ADD_TO_CART_BTN).click()
#
# @then('Verify that there is one item in the cart')
# def verify_items_in_cart(context):
#     actual = context.driver.find_element(*CHECKOUT_CART_CONFIRMATION).text
#     expected = 'Subtotal (1 item):'
#     assert actual == expected, f'Incorrect number of items in the cart, expected {expected}, got {actual}'
#
#
# @then('Verify that Cart is Empty')
# def verify_cart_is_empty(context):
#     actual_result = context.driver.find_element(*CART_TEXT).text
#     expected_result = 'Your Amazon Cart is empty'
#     assert actual_result == expected_result, f'Expected {expected_result}, got {actual_result} instead'
