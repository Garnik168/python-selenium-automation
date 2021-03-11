from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")

    def verify_user_is_on_sign_in_page(self):
        actual_result = self.driver.find_element(*self.SIGN_IN_HEADER).text
        expected_result = "Sign-In"
        assert expected_result == actual_result, f'Expected to see {expected_result} page, got {actual_result} instead'

