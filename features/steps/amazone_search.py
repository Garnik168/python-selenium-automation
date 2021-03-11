from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@when('Input {search_query} into Amazon search field')
def input_amazon_search(context, search_query):
    context.app.main_page.input_amazon_search(search_query)


@when('Click on Amazon search icon')
def click_amazon_search_icon(context):
    context.app.main_page.click_amazon_search_icon()


@then('Product results for {search_query} are shown on Amazon')
def product_results_are_shown(context, search_query):
    context.app.search_results_page.product_results_are_shown(search_query)


@then('Page URL address contains word {query}')
def verify_url_contains_query(context, query):
    context.app.search_results_page.verify_url_contains_query(query)


@when('Search for {search_word}')
def input_search(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word, Keys.ENTER)


