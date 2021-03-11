from behave import when
from selenium.webdriver.common.by import By


# PRODUCT_RESULT = (By.XPATH, "/div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]") #Lana's version
PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[span[@class='a-price']]") #My version, more stable


@when('Click on the first product')
def click_first_product(context):
    context.app.search_results_page.click_first_product()
