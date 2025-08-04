import os
import pytest
driver=None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Select the browser: chrome or firefox"
    )
    parser.addoption(
        "--headless", action="store_true", help="Run tests in headless mode"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions

    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--incognito")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        if headless:
            options.add_argument("--headless=new")  # 'new' is for Chrome 109+
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        raise Exception("Unsupported browser")

    driver.implicitly_wait(4)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' and report.failed:
        driver = item.funcargs.get("browserInstance", None)
        if driver:
            screenshots_dir = os.path.join(os.path.dirname(__file__), "Reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_") + ".png"
            abs_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(abs_path)

            # Embed image in report
            extra.append(pytest_html.extras.image(abs_path))
        else:
            print(" No WebDriver instance found to take screenshot.")

    report.extra = extra


def _capture_screenshot(file_name, driver):
    if driver:
        driver.get_screenshot_as_file(file_name)
    else:
        print("Cannot capture screenshot — WebDriver instance not found.")
