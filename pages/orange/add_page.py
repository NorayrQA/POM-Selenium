from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrangeAdd(BasePage):
    ADD_PAGE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'
    ADD_BUTTON = (By.CLASS_NAME, 'oxd-button--secondary')
