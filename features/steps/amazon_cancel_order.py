from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


HELP_SEARCH_FIELD = (By.ID, 'helpsearch')
SEARCH_RESULT_TEXT = (By.XPATH, "//h1[text()='Cancel Items or Orders']")
# SEARCH_RESULT_TEXT = (By.XPATH, "//div[@class='a-box-inner']//h1[text()='Cancel Items or Orders']") # Longer version


@given('Open Amazon Help page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input "Cancel order" into the help search field')
def input_help_search_field(context):
    help_search_field = context.driver.find_element(*HELP_SEARCH_FIELD)
    help_search_field.send_keys("Cancel order")


@when('Hit Enter button in the help search field')
def hit_enter_button(context):
    help_search_field = context.driver.find_element(*HELP_SEARCH_FIELD)
    help_search_field.send_keys(Keys.ENTER)


@then('Verify that \'Cancel Items or Orders\' text is present')
def verify_search_query_result(context):
    actual_text = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    expected_text = 'Cancel Items or Orders'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text} instead'
