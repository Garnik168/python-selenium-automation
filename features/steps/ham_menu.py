from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep


HAM_MENU = (By.ID, 'nav-hamburger-menu')


@then('Verify hamburger menu icon is visible')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)
    # context.driver.refresh()          # refreshing the page
    # context.driver.find_element(*HAM_MENU)    # making sure that Stale Element exception is avoided

    # print('FIND ELEMENT')
    # element = context.driver.find_element(*HAM_MENU)
    # print(element)
    # print(type(element))

    # print('FIND ELEMENTSSSSSS')
    # elements = context.driver.find_elements(*HAM_MENU)
    # print(elements)
    # print(type(elements))
    #
    # assert len(elements) == 1
