from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Hover over New Arrivals')
def hover_over_new_arrivals(context):
    context.app.product_page.hover_over_new_arrivals()


@then('Verify User sees New Arrival flyout')
def verify_user_see_new_arrival_flyout(context):
    context.app.product_page.verify_user_see_new_arrival_flyout()
