from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from selenium.webdriver.common.keys import Keys


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.XPATH, "//a[@id='nav-orders']//span[@class='nav-line-2']")
    CART = (By.ID, 'nav-cart')
    SEARCH_DROPDOWN = (By.ID, 'searchDropdownBox')

    def open_main_page(self):
        self.open_url('https://www.amazon.com/')

    def input_amazon_search(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)

    def click_amazon_search_icon(self):
        self.click(*self.SEARCH_ICON)

    def select_department(self, alias: str):
        # drop_down = (self.find_element(*self.SEARCH_DROPDOWN))     # or find element separately and add it to Select()
        select = Select(self.find_element(*self.SEARCH_DROPDOWN))    # select = Select(drop_down)
        select.select_by_value(f'search-alias={alias}')            # provide value from option tag (ChromeDev) look dwn
        # from time import sleep          # f' for making it more dynamic or keep it as a string if it cannot be dynamic
        # sleep(5)    # demo purposes

    def click_orders_button(self):
        self.click(*self.ORDERS_BTN)

    def click_on_cart_icon(self):
        self.click(*self.CART)

    def input_query_and_hit_enter(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)  # I couldn't figure out the best way to send_keys(Keys.ENTER)
        self.hit_enter_key(*self.SEARCH_FIELD)             # So I did a work around adding hit_enter_key(f) in base_page

