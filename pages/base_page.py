import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.action_bot import ActionBot
from pages.types import Locator


class BasePage:
    DEFAULT_TIMEOUT = 5

    def __init__(self, driver: WebDriver, timeout: int | None = None) -> None:
        self.driver = driver
        self.timeout = timeout or self.DEFAULT_TIMEOUT
        self.wait = WebDriverWait(driver, self.timeout)
        self.bot = ActionBot(driver, timeout=self.timeout)

    # ----------------------------
    # Internal helpers (private)
    # ----------------------------
    @staticmethod
    def _resolve_step_name(step_name: str | None, fallback: str) -> str:
        return step_name or fallback

    # ----------------------------
    # Finders
    # ----------------------------
    def find_element(self, by: Locator, step_name: str | None = None) -> WebElement:
        label = self._resolve_step_name(step_name, f'Find element: {by}')
        with allure.step(label):
            return self.driver.find_element(*by)

    def find_elements(self, by: Locator, step_name: str | None = None) -> list[WebElement]:
        label = self._resolve_step_name(step_name, f'Find elements: {by}')
        with allure.step(label):
            return self.driver.find_elements(*by)

    # ----------------------------
    # Waits
    # ----------------------------
    def wait_for_element(self, by: Locator, step_name: str | None = None) -> WebElement:
        label = self._resolve_step_name(step_name, f'Wait for element presence: {by}')
        with allure.step(label):
            return self.wait.until(EC.presence_of_element_located(by))

    def wait_for_element_visible(self, by: Locator, step_name: str | None = None) -> WebElement:
        label = self._resolve_step_name(step_name, f'Wait for element visible: {by}')
        with allure.step(label):
            return self.wait.until(EC.visibility_of_element_located(by))

    def is_element_present(self, by: Locator, step_name: str | None = None) -> bool:
        try:
            self.wait_for_element(by, step_name=step_name)
            return True
        except TimeoutException:
            return False

    def wait_for_clickable(self, by: Locator, step_name: str | None = None) -> WebElement:
        label = self._resolve_step_name(step_name, f'Wait for element to be clickable: {by}')
        with allure.step(label):
            return self.wait.until(EC.element_to_be_clickable(by))

    # ----------------------------
    # Navigation
    # ----------------------------
    def load(self, url: str, step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, f'Open URL: {url}')
        with allure.step(label):
            self.driver.get(url)

    def refresh_page(self, step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, 'Refresh current page')
        with allure.step(label):
            self.driver.refresh()

    def hard_refresh_page(self, step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, 'Hard refresh page (location.reload(true))')
        with allure.step(label):
            self.driver.execute_script('location.reload(true);')

    # ----------------------------
    # Context switch / alerts
    # ----------------------------
    def switch_to_frame(self, by: Locator, step_name: str | None = None):
        label = self._resolve_step_name(step_name, f'Switch to frame: {by}')
        with allure.step(label):
            return self.wait.until(EC.frame_to_be_available_and_switch_to_it(by))

    def switch_to_default_content(self, step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, 'Switch to default content')
        with allure.step(label):
            self.driver.switch_to.default_content()

    def alert_handler(self, action: str = 'accept', step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, f'Handle alert with action={action}')
        with allure.step(label):
            alert = self.wait.until(EC.alert_is_present())

            if action == 'accept':
                alert.accept()
                return

            if action == 'dismiss':
                alert.dismiss()
                return

            raise ValueError("action must be 'accept' or 'dismiss'")