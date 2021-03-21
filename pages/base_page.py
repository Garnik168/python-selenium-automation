from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text: str, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_url(self, url):
        self.driver.get(url)

    def verify_text(self, expected_text: str, *locator):
        """
        Search for a webelement, get its text, compare with expected_text
        :param expected_text: Text to be in webelement
        :param locator: Search strategy and locator of webelemnt (ex. (By.ID, 'id') )
        """
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text} instead'

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}'

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        self.wait.until(EC.presence_of_element_located(locator))
        # return self.wait.until(EC.presence_of_element_located(locator)) Why in your Base Page you use RETURN?

    def hit_enter_key(self, *locator):
        self.find_element(*locator).send_keys(Keys.ENTER)

    def wait_for_text_of_an_element(self, *locator, text):
        # self.wait.until(EC.text_to_be_present_in_element(locator, text)), f'Expected {text} to be present'
        self.wait.until(EC.text_to_be_present_in_element_value(locator, text)), f'Expected {text} to be present'

    def wait_until_not_clickable(self, *locator):
        self.wait.until_not(EC.element_to_be_clickable(locator))

    def wait_no_click_clickable(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator))







