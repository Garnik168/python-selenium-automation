from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
FIRST_UNSPONSORED_RESULT = (By.CSS_SELECTOR, ".s-result-item:not(.AdHolder) a .a-price")
NO_THANKS_BTN = (By.ID, 'attachSiNoCoverage-announce')
ALERT = (By.CSS_SELECTOR, "#attachDisplayAddBaseAlert h4")
CART_BTN_POP_UP_SCREEN = (By.ID, 'attach-sidesheet-view-cart-button')
DELETE_BTN_FOR_ITEM = (By.CSS_SELECTOR, "[data-action='delete'] .a-declarative")


@when('Input {search_query} into Amazon search field and hit ENTER')
def input_query_and_hit_enter(context, search_query):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_query, Keys.ENTER)


@when('Click on the first unsponsored result')
def click_on_first_unsponsored_result(context):
    context.driver.find_element(*FIRST_UNSPONSORED_RESULT).click()


@when('Choose No Thanks option for Add ons')
def no_thanks_add_on_option(context):
    context.driver.find_element(*NO_THANKS_BTN).click()
    sleep(2)    # I hope I'll learn a better solution to this


@then('Verify that alert Added to Cart is present')
def verify_add_to_cart_alert(context):
    expected = 'Added to Cart'
    actual = context.driver.find_element(*ALERT).text
    assert expected == actual, f'Expected {expected}, but got {actual} instead'


@when('Click on Cart button on the pop-up screen')
def click_on_cart_btn_pop_up(context):
    context.driver.find_element(*CART_BTN_POP_UP_SCREEN).click()


@when('Click on Delete button under item in the cart')
def click_delete_button_for_item(context):
    context.driver.find_element(*DELETE_BTN_FOR_ITEM).click()


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
