from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    FIRST_UNSPONSORED_RESULT = (By.CSS_SELECTOR, ".s-result-item:not(.AdHolder) a .a-price")
    FIRST_PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[span[@class='a-price']]")
    SELECTED_DPT_CATEGORY = (By.CSS_SELECTOR, "#nav-subnav[data-category='{DPT_SUBSTR}']")

    def _get_locator(self, department: str):
        return [self.SELECTED_DPT_CATEGORY[0], self.SELECTED_DPT_CATEGORY[1].replace('{DPT_SUBSTR}', department)]

    def product_results_are_shown(self, search_query):
        self.verify_text(search_query, *self.RESULT)

    def click_on_first_unsponsored_result(self):
        self.wait_for_element_click(*self.FIRST_UNSPONSORED_RESULT)

    def click_first_product(self):
        self.click(*self.FIRST_PRODUCT_RESULT)

    def verify_department(self, department):
        locator = self._get_locator(department)
        self.wait_for_element_appear(*locator)






