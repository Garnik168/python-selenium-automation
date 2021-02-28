from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip a.nav-action-button")
NAV_TOOLS = (By.ID, 'nav-tools')

@when('Click Sign In from pop-up')
def click_sign_in_popup_btn(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))
    e.click()


@then('Verify Sign In page opens')
def verify_sing_in_page_opens(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'),
                              f'Url {context.driver.current_url} does not include https://www.amazon.com/ap/signin')


    # assert 'https://www.amazon.com/ap/signin' in context.driver.current_url, \
    #     f'Url {context.driver.current_url} does not include https://www.amazon.com/ap/signin'

@then('Verify Sign In is clickable')
def verify_sign_in_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))


@when('Wait for {seconds} sec')
def sleep_sec(context, seconds):
    sleep(int(seconds))


@then('Verify Sign In disappears')
def verify_sign_in_disappears(context):
    # context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_POPUP_BTN))
    context.driver.wait.until_not(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))       # until_not flips the result
    context.driver.find_element(*NAV_TOOLS)  # Makes sure that you are still on the same page

