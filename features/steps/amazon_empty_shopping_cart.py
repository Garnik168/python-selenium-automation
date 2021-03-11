from selenium.webdriver.common.by import By
# should I remove import of By above, as we don't need this too?
from behave import given, when, then

# should I remove two lines below? we really don't need them anymore

# CART = (By.ID, 'nav-cart')
# CART_TEXT = (By.CSS_SELECTOR, 'div.a-column.a-span8.a-span-last h2')


@when('Click on Cart icon')
def click_on_cart_icon(context):
    context.app.main_page.click_on_cart_icon()


@then('Verify that Cart is Empty')
def verify_cart_is_empty(context):
    context.app.cart_page.verify_cart_is_empty()

