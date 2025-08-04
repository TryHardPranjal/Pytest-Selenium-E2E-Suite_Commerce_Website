import json
import logging

import pytest
pytestmark = pytest.mark.smoke
from POM.CheckoutandConfimationPage import Checkout_confirmtion
from POM.LoginPage import LoginPage
from POM.ShopPage import ShopPage

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

file_path_data='C:/DemoFramework/Data/E2Edata.json'
with open(file_path_data) as f:
    test_data = json.load(f)
    test_list=test_data["data"][0]
    invalid_user = {
        "username": "invaliduser",
        "password": "wrongpass"
    }

#Test case 1-Valid User Login Test case
@pytest.mark.suite
@pytest.mark.smoke
def test_valid_login(browserInstance):
    logger.info("Launching valid login test...")

    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    login_page.assert_title()

    login_page.login(test_list["username"], test_list["password"])
    logger.info("Valid credentials entered.")
    login_page.wait_until_title_contains("ProtoCommerce")
    actual_title = driver.title
    expected_title = "ProtoCommerce"
    assert expected_title in actual_title, f"[LoginPage] Expected '{expected_title}' in '{actual_title}'"
    logger.info("Valid login test passed.")

#Test case 2-InValid User Login with Empty Username and Password entered
@pytest.mark.suite
@pytest.mark.smoke
def test_invalid_login_empty_credentials(browserInstance):
    logger.info("Launching invalid login test with empty credentials...")

    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    login_page.assert_title()

    login_page.login("", "")
    logger.info("Empty credentials entered.")

    error_text = login_page.get_login_error_message()
    print(error_text)
    expected_error = "Empty username/password"
    assert expected_error in error_text, f"[LoginPage] Expected error '{expected_error}', but got '{error_text}'"
    logger.info("Invalid login test with empty credentials passed.")


# Test case 3 - Invalid Login with Incorrect Credentials
@pytest.mark.suite
@pytest.mark.smoke
def test_invalid_login_incorrect_credentials(browserInstance):
    logger.info("Launching invalid login test with incorrect credentials...")

    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    login_page.assert_title()

    # Enter invalid username and password
    login_page.login("wronguser", "wrongpass")
    logger.info("Incorrect credentials entered.")

    error_text = login_page.get_login_error_message()
    print(f"Captured error text: {error_text}")
    expected_error = "Incorrect username/password"
    assert expected_error in error_text, f"[LoginPage] Expected error '{expected_error}', but got '{error_text}'"
    logger.info("Invalid login test with incorrect credentials passed.")

#Test case 4-Valid Product Add to Cart and Validate
#After login, verify that the selected product appears in the cart in the checkout page.
@pytest.mark.suite
@pytest.mark.smoke
def test_add_product_to_cart_and_validate(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    login_page.assert_title()
    login_page.login(test_list["username"], test_list["password"])
    Shop_page = ShopPage(driver)
    Shop_page.add_products_to_cart(test_list["productName"])
    Shop_page.got_to_Checkout_page()
    checkout = Checkout_confirmtion(driver)
    assert checkout.is_product_in_cart("Blackberry"), "Product 'Blackberry' not found in checkout cart."
    logger.info("Product 'Blackberry' successfully verified in checkout cart.")



