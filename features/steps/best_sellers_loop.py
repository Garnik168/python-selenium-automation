from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

MENU_TABS = (By.CSS_SELECTOR, '#zg_tabs a')
BANNER = (By.ID, 'zg_banner_text_wrapper')


@then('Verify that user can go though all best sellers menu tabs and correct corresponding page opens')
def click_on_best_sellers_menu_tabs_and_verify_page(context):
    menu_tabs = context.driver.find_elements(*MENU_TABS)        # I need it to know how many tabs I should loop through
    for tab in range(0, len(menu_tabs)):
        working_tab = context.driver.find_elements(*MENU_TABS)[tab]    # This does the trick :)
        expected = working_tab.text
        working_tab.click()
        actual = context.driver.find_element(*BANNER).text
        assert expected in actual, f'Expected {expected}, but got {actual} instead'




