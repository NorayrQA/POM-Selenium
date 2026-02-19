from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_firefox_driver():
    """
    Initializes and returns a Firefox WebDriver instance.

    Configured for Ubuntu/Snap environments where the binary path
    often needs to be explicitly defined.

    Returns:
        WebDriver instance: Configured Firefox driver.
    """
    options = FirefoxOptions()

    # Path to the Firefox binary, required for Snap versions where it's not auto-detected.
    options.binary_location = '/snap/firefox/current/usr/lib/firefox/firefox'

    # Add any specific Chrome options here (e.g., headless mode, incognito, etc.)
    # options.headless = True  # Uncomment to run Chrome in headless mode

    try:
        # Attempt to initialize the Firefox WebDriver
        driver = webdriver.Firefox(options=options)
        return driver
    except Exception as e:
        # Log error and return None if driver initialization fails
        print(f"Failed to initialize Firefox driver: {e}")
        return None