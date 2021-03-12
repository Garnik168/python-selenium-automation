from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Lana's version


# ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button') # Already have it in another .py is it okay just to leve it on one place and as logn as the name is matching it will always be able to acces it even from another .py of the same steps folder right?
CART_COUNT = (By.ID, 'nav-cart-count')
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
SIZE_OPTION_0 = (By.ID, 'size_name_0')
BUY_NOW_BTN = (By.ID, 'buy-now-button')       # This element appears before we can click on add to cart,
# hopefully will fix the explicit wait error


# @when('Click on Add to Cart button') # my version from different .py file hashed to avoid selenium confusion
# def click_add_to_cart(context):
#     context.driver.find_element(*ADD_TO_CART_BTN).click()


# @when('Click on Add to Cart button (Lana\'s version)')            # Keeping this here for future reference
# def click_add_to_cart_lana(context):
#     context.driver.find_element(*ADD_TO_CART_BTN).click()
#     if len(context.driver.find_elements(*SIZE_TOOLTIP)) == 1:
#         context.driver.find_element(*SIZE_SELECTION_BTN).click()
#         context.driver.find_element(*SIZE_OPTION_0).click()
#         sleep(2)
#         context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('Click on Add to Cart button (Lana\'s version)')
def click_add_to_cart_lana(context):
    context.app.product_page.click_add_to_cart_lana()
    # # sleep(2)    # Hashed, I couldn't find one line solution, but I got the work around option, see below
    # context.driver.wait.until(EC.presence_of_element_located(BUY_NOW_BTN))       # This is my work around, but I'm
    # # pretty sure there are much better and more effective solutions, please share :)
    # e = context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN))    # Extra practice
    # e.click()
    # # context.driver.find_element(*ADD_TO_CART_BTN).click()     # Or this line if you hash the two lines above


@when('Select item\'s size')
def select_size(context):
    context.app.product_page.select_size()
    # context.driver.find_element(*SIZE_SELECTION_BTN).click()
    # context.driver.find_element(*SIZE_OPTION_0).click()
    # # sleep(2)    # Had to add this, otherwise fails, can't wait to learn better way of doing so
    # # Explicit wait is not required for this section, cuz the action has to be after this step


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    context.app.cart_page.verify_cart_count(expected_count)


