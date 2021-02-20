from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@when('Input {search_query} into Amazon search field')
def input_amazon_search(context, search_query):
    search_field = context.driver.find_element(*SEARCH_FIELD)
    search_field.send_keys(search_query)


@when('Click on Amazon search icon')
def click_amazon_search_icon(context):
    search_icon_button = context.driver.find_element(*SEARCH_ICON)
    search_icon_button.click()


@then('Product results for {search_query} are shown on Amazon')
def product_results_are_shown(context, search_query):
    actual_text = context.driver.find_element(*RESULT).text
    expected_text = f'{search_query}'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text} instead'


@then('Page URL address contains word {query}')
def verify_url_contains_query(context, query):
   assert query in context.driver.current_url, f'{query} not in {context.driver.current_url}'


@when('Search for {search_word}')
def input_search(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word, Keys.ENTER)


