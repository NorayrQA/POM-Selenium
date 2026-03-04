from utils import constans
from pages.saucedemo.login_page import LoginPage
from tests.conftest import driver

class TestLogin:
    def test_saucedemo_login(self, driver, logged_in_driver):
       login_page = LoginPage(driver)
       login_page.login(constans.LOGIN_USERNAME, constans.LOGIN_PASSWORD)

       assert login_page.get_success_message() == 'Swag Labs'


