from behave import when, then, given
from selenium.webdriver.common.by import By


BENEFIT_BOXES = (By.CSS_SELECTOR, ".benefit-box")

@given('Open Amazon Prime page')
def open_amazon_prime_page(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('Verify {expected_boxes_count} benefit boxes are present')
def verify_benefit_boxes_present(context, expected_boxes_count):
    # actual_boxes = len(context.driver.find_elements(*BENEFIT_BOXES))
    # expected_boxes = 8
    # assert actual_boxes == expected_boxes, f'Expected {expected_boxes}, but got {actual_boxes} instead'
    # Lana's version
    actual_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(actual_boxes) == int(expected_boxes_count), f'Expected {expected_boxes_count}, but got {actual_boxes} instead'