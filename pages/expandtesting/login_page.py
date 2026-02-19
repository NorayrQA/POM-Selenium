from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    login_page_url = 'https://practice.expandtesting.com/login'
    username_locator = (By.ID, 'username')
    password_locator = (By.ID, 'password')
    submit_button_locator = (By.ID, 'submit-login')
    success_login_locator = (By.XPATH, "//b[text()='You logged into a secure area!']")
    success_login_text = 'You logged into a secure area!'

    def login_page_load(self):
        self.load(self.login_page_url)

    def type_username(self, username):
        self.bot.type(self.username_locator, username)

    def type_password(self, password):
        self.bot.type(self.password_locator, password)

    def click_submit_button(self):
        self.bot.click(self.submit_button_locator)

    def is_login_successful(self):
        return self.success_login_text == self.bot.element_text(self.success_login_locator)

    def login(self, username, password):
        self.login_page_load()
        self.bot.scroll_by_amount(0, 800)
        self.type_username(username)
        self.type_password(password)
        self.click_submit_button()

        assert self.is_login_successful(), 'Login failed.'

