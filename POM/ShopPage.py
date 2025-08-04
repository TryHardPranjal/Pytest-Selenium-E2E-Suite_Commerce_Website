from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.Shop_link=(By.LINK_TEXT,"Shop")
        self.products_carts=(By.XPATH, "//div[@class='card h-100']")
        self.checkout_link=(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")

    def open_shop_page(self):
        self.wait_until_present(self.Shop_link)
        self.assert_title_contains("ProtoCommerce", context="ShopPage")

    def add_products_to_cart(self,products_names):
        self.driver.find_element(*self.Shop_link).click()
        self.open_shop_page()

        mobiles = self.driver.find_elements(*self.products_carts)

        for mobile in mobiles:
            name_of_Mobiles = mobile.find_element(By.XPATH, "div/h4/a").text
            if name_of_Mobiles == products_names:
                mobile.find_element(By.XPATH, "div/button").click()
                break

    def got_to_Checkout_page(self):
        self.driver.find_element(*self.checkout_link).click()