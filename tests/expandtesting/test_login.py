from pages.expandtesting.login_page import LoginPage
from tests.conftest import driver


class TestLogin:
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login('practice', 'SuperSecretPassword!')

