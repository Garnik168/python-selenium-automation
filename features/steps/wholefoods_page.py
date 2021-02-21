from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


REGULAR_TAG = (By.CSS_SELECTOR, 'ul.s-col-3 span[class*="regular-price"]')
PRODUCT_NAME = (By.CSS_SELECTOR, 'ul.s-col-3 span[class*="product-name"]')


@given('Open Wholefoods Deals page')
def open_wholefoods_deals_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify that all products under yellow banner have Regular tags')
def verify_regular_tag(context):
    expected_tag = 'Regular'
    product_list = context.driver.find_elements(*REGULAR_TAG)
    for element in range(len(product_list)):
        actual_product_text = product_list[element].text
        assert expected_tag in actual_product_text, f'Expected {expected_tag} to be present in {actual_product_text}'


@then('Verify that all products under yellow banner have names')
def verify_products_have_names(context):
    # context.driver.wait.until(EC.visibility_of_all_elements_located(PRODUCT_NAME))     # But I don't know how to check
    # that it really checks all of them

    product_list = context.driver.find_elements(*PRODUCT_NAME)
    for product in range(len(product_list)):
        actual_product_name = product_list[product].text
        # assert type(actual_product_name) == str, f' {actual_product_name} doesn\'t look like a product name to me'
        # assert actual_product_name.isalnum() or '' in actual_product_name or, \
        #     f' {actual_product_name} doesn\'t look like a product name to me'     # This one sure looks more stable

        # this one is probably the most stable:
        assert actual_product_name.isprintable(), f' {actual_product_name} doesn\'t look like a product name to me'
# I'm still not sure which is the best way to verify that the name is a real product name, I can only so far check
# that it is a string, or if it has specific properties as a string....
# so I'm confused at this point, but I think overall my solution works. What would be considered the best practice?
# How should I approach this types of tests in the future?
