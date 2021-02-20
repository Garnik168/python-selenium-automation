from behave import given, when, then
from selenium.webdriver.common.by import By


COLOR_IMG = (By.CSS_SELECTOR, '#variation_color_name li')
COLOR_NAMES = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_amazon_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@then("Verify user's selected colors clicking through them")
def verify_jeans_colors(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage',
                       'Light Wash', 'Medium Vintage', 'Medium Wash', 'Rinse', 'Rinsed Vintage', 'Vintage Light Wash',
                       'Washed Black']
    colors = context.driver.find_elements(*COLOR_IMG)
    for element in range(len(colors)):
        colors[element].click()
        selected_color = context.driver.find_element(*COLOR_NAMES).text
        assert expected_colors[element] == selected_color, f'Expected {expected_colors[element]}, ' \
                                                           f'but got {selected_color} instead'
