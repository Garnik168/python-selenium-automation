from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    FIRST_UNSPONSORED_RESULT = (By.CSS_SELECTOR, ".s-result-item:not(.AdHolder) a .a-price")
    FIRST_PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[span[@class='a-price']]")

    def product_results_are_shown(self, search_query):
        self.verify_text(search_query, *self.RESULT)

    def click_on_first_unsponsored_result(self):
        self.wait_for_element_click(*self.FIRST_UNSPONSORED_RESULT)

    def click_first_product(self):
        self.click(*self.FIRST_PRODUCT_RESULT)





