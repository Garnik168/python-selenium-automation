from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


APPLICATION_LINK = (By.CSS_SELECTOR, "a[href*='feature']")
DOWNLOAD_THE_APP_MESSAGE = (By.ID, 'mgt-email-sms-download-header')


@given('Open Amazon T&C page')
def open_amazon_terms_and_cond_page(context):
    context.driver.get(f'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of'
                       f'_use?ie=UTF8&nodeId=508088')


@when('Click on Amazon applications link')
def click_on_amazon_app_link(context):
    context.driver.find_element(*APPLICATION_LINK).click()


@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.driver.switch_to_window(context.driver.window_handles[1])


@then('Verify that Amazon app page is opened')
def verify_amazon_app_page_is_open(context):
    actual = context.driver.find_element(*DOWNLOAD_THE_APP_MESSAGE).text
    expected = 'Download the app today!'
    assert actual == expected, f'Expected {expected}, but got {actual} instead'


@then('User can close new window and switch back to original')
def close_new_window_and_switch_back_to_original(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)

