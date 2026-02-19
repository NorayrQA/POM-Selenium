import allure
from selenium.common.exceptions import UnexpectedTagNameException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from pages.types import Locator


class ActionBot:
    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ----------------------------
    # Internal helpers (private)
    # ----------------------------
    @staticmethod
    def _resolve_step_name(step_name: str | None, fallback: str) -> str:
        return step_name or fallback

    def _wait_present(self, by: Locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(by))

    def _wait_clickable(self, by: Locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(by))

    def _get_select(self, by: Locator) -> Select:
        element = self._wait_present(by)
        try:
            return Select(element)
        except UnexpectedTagNameException as e:
            raise TypeError(
                f'Locator {by} is not a <select> element. '
                f'If this is a custom dropdown, use click-based selection.'
            ) from e

    # ----------------------------
    # Public actions
    # ----------------------------
    def click(self, by: Locator, step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, f'Click element: {by}')
        with allure.step(label):
            self._wait_clickable(by).click()

    def type(self, by: Locator, text: str, step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, f'Type text into element: {by}')
        with allure.step(label):
            self._wait_present(by).send_keys(text)

    def clear_and_type(self, by: Locator, text: str, step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, f'Clear and type text into element: {by}')
        with allure.step(label):
            element = self._wait_present(by)
            element.clear()
            element.send_keys(text)

    def element_text(self, by: Locator, step_name: str | None = None) -> str:
        label = self._resolve_step_name(step_name, f'Get element text: {by}')
        with allure.step(label):
            return self._wait_present(by).text

    def scroll_to_element(self, by: Locator, step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, f'Scroll to element: {by}')
        with allure.step(label):
            element = self._wait_present(by)
            ActionChains(self.driver).scroll_to_element(element).perform()

    def scroll_by_amount(self, x: int, y: int, step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, f'Scroll by amount x={x}, y={y}')
        with allure.step(label):
            ActionChains(self.driver).scroll_by_amount(x, y).perform()

    def scroll_from_element(
            self,
            by: Locator,
            x: int,
            y: int,
            step_name: str | None = None,
    ) -> None:
        label = self._resolve_step_name(step_name,f'Scroll from element {by} by x={x}, y={y}')
        with allure.step(label):
            element = self._wait_present(by)
            scroll_origin = ScrollOrigin.from_element(element)
            ActionChains(self.driver).scroll_from_origin(scroll_origin, x, y).perform()

    def select_by_visible_text(self, by: Locator, text: str, step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, f'Select option by visible text "{text}": {by}')
        with allure.step(label):
            self._get_select(by).select_by_visible_text(text)

    def select_by_value(self, by: Locator, value: str, step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, f'Select option by value "{value}": {by}')
        with allure.step(label):
            self._get_select(by).select_by_value(value)

    def select_by_index(self, by: Locator, index: int, step_name: str | None = None) -> None:
        label = self._resolve_step_name(step_name, f'Select option by index {index}: {by}')
        with allure.step(label):
            self._get_select(by).select_by_index(index)

    def get_selected_option_text(self, by: Locator, step_name: str | None = None) -> str:
        label = self._resolve_step_name(step_name, f'Get selected option text: {by}')
        with allure.step(label):
            return self._get_select(by).first_selected_option.text

    def get_all_option_texts(self, by: Locator, step_name: str | None = None) -> list[str]:
        label = self._resolve_step_name(step_name, f'Get all option texts: {by}')
        with allure.step(label):
            select = self._get_select(by)
            return [option.text for option in select.options]

