from pytest_bdd import scenarios, given, when, then
import json
import logging
from POM.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Logging setup
logger = logging.getLogger(__name__)

# Load data from JSON
file_path = 'C:/DemoFramework/Data/E2Edata.json'
with open(file_path) as f:
    data = json.load(f)
    valid_user = data["data"][0]  # Using the first user

# Link to the feature file
scenarios('../Features/login.feature')


@given("the user launches the application")
def launch_application(browserInstance):
    browserInstance.get("https://rahulshettyacademy.com/loginpagePractise/")
    logger.info("Application launched.")
    return browserInstance


@when("the user enters valid credentials")
def enter_credentials(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.login(valid_user["username"], valid_user["password"])
    logger.info("Entered valid credentials.")


@then("the user should land on the homepage")
def verify_home(browserInstance):
    expected_title = "ProtoCommerce"

    # Wait until the title contains the expected text (max 10 seconds)
    WebDriverWait(browserInstance, 10).until(
        EC.title_contains(expected_title)
    )

    actual_title = browserInstance.title
    assert expected_title in actual_title, f"[LoginPage] Expected '{expected_title}' in '{actual_title}'"
    logger.info("User successfully landed on homepage.")