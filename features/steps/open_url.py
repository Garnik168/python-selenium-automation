from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()
