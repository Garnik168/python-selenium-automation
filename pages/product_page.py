from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    # NO_THANKS_BTN = (By.ID, 'attachSiNoCoverage-announce')    # dif may be it could fix it
    NO_THANKS_BTN = (By.ID, 'attachSiNoCoverage')               # THIS locator fixes the problem with sleep
    # ALERT = (By.CSS_SELECTOR, "#attachDisplayAddBaseAlert h4")
    ALERT = (By.CSS_SELECTOR, "#attach-added-to-cart-message h4")   # dif selector could fix the issue
    CART_BTN_POP_UP_SCREEN = (By.ID, 'attach-sidesheet-view-cart-button')
    BUY_NOW_BTN = (By.ID, 'buy-now-button')
    SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
    SIZE_OPTION_0 = (By.ID, 'size_name_0')

    def click_add_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)

    def no_thanks_add_on_option(self):
        self.wait_for_element_click(*self.NO_THANKS_BTN)
        self.wait_element_disappear(*self.NO_THANKS_BTN)
        # self.wait_until_not_clickable(*self.NO_THANKS_BTN)

    def verify_add_to_cart_alert(self, text):
        self.wait_no_click_clickable(*self.CART_BTN_POP_UP_SCREEN)
        self.verify_text(text, *self.ALERT)
        # wait is needed

    def click_on_cart_btn_pop_up(self):
        self.wait_for_element_click(*self.CART_BTN_POP_UP_SCREEN)

    def click_add_to_cart_lana(self):
        self.wait_no_click_clickable(*self.BUY_NOW_BTN)   # for some reason wait_for_element_appear doesn't work
        self.click(*self.ADD_TO_CART_BTN)

    def select_size(self):
        self.driver.find_element(*self.SIZE_SELECTION_BTN).click()
        self.driver.find_element(*self.SIZE_OPTION_0).click()


