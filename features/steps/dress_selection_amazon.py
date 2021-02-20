from behave import given, when, then
from selenium.webdriver.common.by import By


COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon Dress {productid} page')
def open_dress_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}')


@then('Verify user can click through colors')
def verify_can_select_colors(context):
    expected_colors = ['Emerald', 'Ivory', 'Navy']
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(colors)):
        colors[i].click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert expected_colors[i] == selected_color, f'Expected {expected_colors[i]}, but got {selected_color} instead'



