from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrangeLogin(BasePage):
    LOGIN_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    USERNAME_LOCATOR = (By.NAME, "username")
    PASSWORD_LOCATOR = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, 'oxd-button')
    SUCCESS_LOGIN = (By.XPATH, '//h6[text()="Dashboard"]')
    SUCCESS_LOGIN_TEXT = 'Dashboard'

    def page_load(self):
        self.load(self.LOGIN_URL)

    def type_username(self, username):
        self.bot.type(self.USERNAME_LOCATOR, username)

    def type_password(self, password):
        self.bot.type(self.PASSWORD_LOCATOR, password)

    def click_login_button(self):
        self.bot.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        return self.SUCCESS_LOGIN_TEXT == self.bot.element_text(self.SUCCESS_LOGIN)

