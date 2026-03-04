from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import constans

class LoginPage(BasePage):
    LOGIN_PAGE_URL = 'https://www.saucedemo.com/'
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    SUCCESS_LOGIN = (By.CLASS_NAME, 'app_logo')

    def load_page(self):
        self.load(self.LOGIN_PAGE_URL)

    def type_username(self, username):
        self.bot.type(self.USERNAME, username)

    def type_password(self, password):
        self.bot.type(self.PASSWORD, password)

    def click_login_button(self):
        self.bot.click(self.LOGIN_BUTTON)

    def get_success_message(self):
        return self.bot.element_text(self.SUCCESS_LOGIN)

    def login(self, username, password):
        self.load_page()
        self.type_username(username)
        self.type_password(password)
        self.click_login_button()

    def is_logged_in(self, timeout: int | None = None) -> bool:
        try:
            text = self.bot.element_text(self.SUCCESS_LOGIN).strip()
            return text == constans.SUCCESS_MESSAGE
        except TimeoutException:
            return False



