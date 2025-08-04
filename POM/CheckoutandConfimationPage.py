from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.browserutils import BrowserUtils


class Checkout_confirmtion(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button=(By.CSS_SELECTOR, "button[class='btn btn-success']")
        self.enter_ini_country=(By.ID, "country")
        self.check_named_Country=(By.LINK_TEXT, "India")
        self.select_Checkbox=(By.CSS_SELECTOR, "label[for='checkbox2']")
        self.success_message_locator=(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")
        self.wait = WebDriverWait(self.driver, 10)
        self.purchase_button=(By.CSS_SELECTOR, "input[value=Purchase]")


    def go_to_Checkout_page(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self,country_first3_letters):
        self.driver.find_element(*self.enter_ini_country).send_keys(country_first3_letters)

        self.wait_until_present(self.check_named_Country)
        self.driver.find_element(*self.check_named_Country).click()

    def validate_order(self):
        self.driver.find_element(*self.purchase_button).click()
        self.wait_until_present(self.success_message_locator)
        Success_msg = self.driver.find_element(*self.success_message_locator).text
        element = self.driver.find_element(*self.success_message_locator)
        Success_text = element.get_attribute("innerText").replace("×", "").strip()
        print(f"Order Confirmation: {Success_text}")
        assert "Success! Thank you!" in Success_msg

    def is_product_in_cart(self, expected_product):
        rows = self.driver.find_elements(By.XPATH, "//tr")
        for row in rows:
            try:
                product_name = row.find_element(By.XPATH, ".//h4[@class='media-heading']/a").text
                if expected_product.lower() in product_name.lower():
                    return True
            except:
                continue
        return False
