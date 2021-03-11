from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_TEXT = (By.CSS_SELECTOR, 'div.a-column.a-span8.a-span-last h2')
    CHECKOUT_CART_CONFIRMATION = (By.ID, 'sc-subtotal-label-buybox')
    DELETE_BTN_FOR_ITEM = (By.CSS_SELECTOR, "[data-action='delete'] .a-declarative")

    def verify_cart_is_empty(self):
        actual_result = self.driver.find_element(*self.CART_TEXT).text
        expected_result = 'Your Amazon Cart is empty'
        assert actual_result == expected_result, f'Expected {expected_result}, got {actual_result} instead'

    def verify_items_in_cart(self):
        actual = self.driver.find_element(*self.CHECKOUT_CART_CONFIRMATION).text
        expected = 'Subtotal (1 item):'
        assert actual == expected, f'Incorrect number of items in the cart, expected {expected}, got {actual}'

    def click_delete_button_for_item(self):
        self.wait_for_element_click(*self.DELETE_BTN_FOR_ITEM)


