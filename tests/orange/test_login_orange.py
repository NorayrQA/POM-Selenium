from pages.orange.orange_page import OrangeLogin


class TestLogin:
    def test_login(self, driver):
        orange_page = OrangeLogin(driver)
        orange_page.page_load()
        orange_page.type_username('Admin')
        orange_page.type_password('admin123')
        orange_page.click_login_button()

        assert orange_page.is_login_successful(), 'Login failed.'

