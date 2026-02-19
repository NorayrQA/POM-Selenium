from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_driver():
    """
    Initializes and returns a Chrome WebDriver instance.

    Returns:
        WebDriver instance: Configured Chrome driver.
    """
    options = Options()

    # Add any specific Chrome options here (e.g., headless mode, incognito, etc.)
    # options.headless = True  # Uncomment to run Chrome in headless mode

    try:
        # Initialize the Chrome WebDriver with options
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()  # Maximize window for better visibility
        return driver
    except Exception as e:
        # Log error if driver initialization fails
        print(f"Failed to initialize Chrome driver: {e}")
        return None