import json
import logging

import pytest

from POM.CheckoutandConfimationPage import Checkout_confirmtion
from POM.LoginPage import LoginPage
from POM.ShopPage import ShopPage

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

file_path_data = 'C:/DemoFramework/Data/E2Edata.json'
with open(file_path_data) as f:
    test_data = json.load(f)
    test_list = test_data["data"]
    invalid_user = {
        "username": "invaliduser",
        "password": "wrongpass"
    }

#Test case 5 Regression with parametrization - Validate Order Success with whole flow
@pytest.mark.suite
@pytest.mark.regression
@pytest.mark.parametrize("test_list_item",test_list)
def test_End2EndParametrizetest(browserInstance, test_list_item):
    driver = browserInstance
    logger.info("Launching login page...")
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login=LoginPage(driver)
    login.assert_title()
    login.login(test_list_item["username"],test_list_item["password"])
    Shop_page=ShopPage(driver)
    Shop_page.add_products_to_cart(test_list_item["productName"])
    Shop_page.got_to_Checkout_page()

    Check_and_confirm=Checkout_confirmtion(driver)
    assert "ProtoCommerce" in Check_and_confirm.get_title()
    Check_and_confirm.go_to_Checkout_page()
    Check_and_confirm.enter_delivery_address("ind")
    Check_and_confirm.validate_order()
    logger.info("Test completed successfully.")