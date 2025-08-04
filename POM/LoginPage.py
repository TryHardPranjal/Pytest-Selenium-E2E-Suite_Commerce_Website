from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username=(By.ID, "username")
        self.password=(By.ID, "password")
        self.signin_button=(By.ID,"signInBtn")
        self.error_message = (By.CSS_SELECTOR, "div.alert.alert-danger")



    def login(self,username,password,):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signin_button).click()


    def get_title(self):
        return self.driver.title

    def assert_title(self, expected="LoginPage Practise | Rahul Shetty Academy"):
        actual = self.get_title()
        assert expected in actual, f"[LoginPage] Expected title '{expected}' but got '{actual}'"

    def get_login_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        ).text
