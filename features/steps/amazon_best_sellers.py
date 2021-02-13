from behave import when, then, given
from selenium.webdriver.common.by import By


BEST_SELLER_5_LINKS = (By.CSS_SELECTOR, '#zg_tabs a')


@given('Open Amazon Best Sellers page')
def open_amazon_best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify {links_count} Best Sellers links are present')
def verify_best_sellers_links(context, links_count):
    context.driver.find_elements(*BEST_SELLER_5_LINKS)
    expected = int(links_count)
    actual = len(context.driver.find_elements(*BEST_SELLER_5_LINKS))
    assert actual == expected, f'Expected {expected} links, got {actual} instead'
