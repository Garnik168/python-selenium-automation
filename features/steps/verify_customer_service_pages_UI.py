from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

WHAT_CAN_WE_HELP_YOU_WITH_TEXT = (By.CSS_SELECTOR, "h1")
SOME_THING_YOU_CAN_DO_HERE_HEADER = (By.CSS_SELECTOR, ".ss-landing-container-wide h2")
SELF_SERVICE_RICH_CARD = (By.CSS_SELECTOR, "a .self-service-rich-card")
SEARCH_HELP_LIBRARY_SECTION = (By.CSS_SELECTOR, "#help-search-label .a-text-bold")
SEARCH_HELP_LIBRARY_INPUT_FIELD = (By.ID, 'helpsearch')
BROWSE_HELP_TOPICS_TEXT = (By.CSS_SELECTOR, "div.a-column h1")
BROWSE_HELP_TOPIC_LINKS = (By.CSS_SELECTOR, "a[rel*='#help-gateway-category']")
BROWSE_HELP_TOPIC_IMAGES = (By.CSS_SELECTOR, "img.csg-hb-promo")


@given('Open Amazon Customer Service Help page')
def open_amazon_customer_srv_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('Verify that Hello. What can we help you with line is present')
def verify_what_can_we_help_you_with_text(context):
    actual = context.driver.find_element(*WHAT_CAN_WE_HELP_YOU_WITH_TEXT).text
    expected = 'Hello. What can we help you with?'
    assert expected == actual, f'Expected {expected}, but got {actual} instead'


@then('Verify that Some things you can do here section is present')
def verify_some_things_you_can_do_here_section(context):
    actual = context.driver.find_element(*SOME_THING_YOU_CAN_DO_HERE_HEADER).text
    expected = 'Some things you can do here'
    assert expected == actual, f'Expected {expected}, but got {actual}, instead'


@then('Verify that Some things you can do here section contains {cards_count} self service rich cards')
def verify_self_service_rich_cards_are_present(context, cards_count):
    actual = len(context.driver.find_elements(*SELF_SERVICE_RICH_CARD))
    expected = int(cards_count)
    assert expected == actual, f'Expected {expected}, but got {actual}, instead'


@then('Verify that Search Help Library section is present')
def verify_search_help_library_section(context):
    actual = context.driver.find_element(*SEARCH_HELP_LIBRARY_SECTION).text
    expected = 'Search the help library'
    assert expected == actual, f'Expected {expected}, but got {actual}, instead'


@then('Verify that Search Help Library input field is present')
def verify_search_help_library_input_field_present(context):
    actual = len(context.driver.find_elements(*SEARCH_HELP_LIBRARY_INPUT_FIELD))    # Using find_elementS just for extra practice :)
    expected = 1
    assert expected == actual, f'Expected {expected}, but got {actual}, instead'


@then('Verify that Browse Help Topics section is present')
def verify_browse_help_topics_section(context):
    actual = context.driver.find_element(*BROWSE_HELP_TOPICS_TEXT).text
    expected = 'Browse Help Topics'
    assert expected == actual, f'Expected {expected}, but got {actual}, instead'


@then('Verify that Browse Help Topics section contains {links_count} help getaway links')
def verify_browser_help_popular_topic_links(context, links_count):
    actual = len(context.driver.find_elements(*BROWSE_HELP_TOPIC_LINKS))
    expected = int(links_count)
    assert expected == actual, f'Expected {expected}, but got {actual}, instead'


@then('Verify that image is present in Browse Help Topics')
def verify_img_present(context):
    context.driver.find_element(*BROWSE_HELP_TOPIC_IMAGES)


