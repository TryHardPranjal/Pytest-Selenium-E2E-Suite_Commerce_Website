from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BrowserUtils:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def get_title(self):
        return self.driver.title

    def wait_until_present(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )
    def assert_title_contains(self, expected, context=""):
        actual = self.driver.title
        assert expected in actual, f"[{context}] Expected title to contain '{expected}', but got '{actual}'"

    def wait_until_title_contains(self, partial_title):
        WebDriverWait(self.driver, self.timeout).until(
            EC.title_contains(partial_title)
        )

