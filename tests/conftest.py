import pytest
import allure
from utils.firefox_driver import get_firefox_driver
from utils.chrome_driver import get_chrome_driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to attach screenshots and exception messages on test failure."""
    outcome = yield
    rep = outcome.get_result()

    # Only handle failed tests
    if rep.when != 'call' or not rep.failed:
        return

    driver = item.funcargs.get('driver')

    # Capture screenshot on failure
    if driver:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f'failure_screenshot_{item.name}',
            attachment_type=allure.attachment_type.PNG
        )

    # Attach exception message if available
    if call.excinfo:
        allure.attach(
            str(call.excinfo.value),
            name=f'exception_{item.name}',
            attachment_type=allure.attachment_type.TEXT
        )


@pytest.fixture(scope="session")
def driver(request):
    """Fixture to provide a WebDriver instance based on the requested browser."""
    browser = request.config.getoption("--browser", default="chrome")

    # Initialize the driver based on the selected browser
    if browser == "firefox":
        driver = get_firefox_driver()
    elif browser == "chrome":
        driver = get_chrome_driver()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()  # Maximize window for better visibility
    yield driver
    driver.quit()  # Ensure the driver is quit after the test session