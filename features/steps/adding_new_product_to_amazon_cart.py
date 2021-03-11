from selenium.webdriver.common.by import By
from behave import given, when, then


PRODUCT_PAGE = 'https://www.amazon.com/Apple-MHXH3AM-A-MagSafe-Charger/dp/B08L5NP6NG/ref=pd_cart_vw_crc_1_1/132-9822274-2448127?_encoding=UTF8&pd_rd_i=B08L5NP6NG&pd_rd_r=912e1cd3-e599-49d6-97a0-0214c396cccb&pd_rd_w=ziZmK&pd_rd_wg=coag0&pf_rd_p=01004c92-8f40-4f1a-bee8-08cb36dccac2&pf_rd_r=VK19ZF4SD1QWV5ZAK0DH&psc=1&refRID=VK19ZF4SD1QWV5ZAK0DH'
POP_UP_CONFIRMATION = (By.ID, 'huc-v2-order-row-confirm-text')
CART = (By.ID, 'nav-cart')


@given('Open Apple Mag Safe Charger page on Amazon')
def open_product_page(context):
    context.driver.get(PRODUCT_PAGE)


@then('Check that confirmation pop-up is present')
def check_confirmation(context):
    actual = context.driver.find_element(*POP_UP_CONFIRMATION).text
    expected = 'Added to Cart'
    assert actual == expected, f'Confirmation Pop-up didn\'t work'


@when('Click on Cart')
def click_on_cart(context):
    context.driver.find_element(*CART).click()







