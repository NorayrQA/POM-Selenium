from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RowPage(BasePage):
    TEST_URL = 'https://practicetestautomation.com/practice-test-exceptions/'
    ADD_BUTTON = (By.ID, 'add_btn')
    SUCCESS_MESSAGE = (By.ID, 'confirmation')
    ROW_2 = (By.ID, 'row2')
    INPUT_ROW_2 = (By.CSS_SELECTOR, '#row2 input.input-field')
    SAVE_BUTTON = (By.CSS_SELECTOR, '#row2 button#save_btn')
    EDIT_BUTTON = (By.ID, 'edit_btn')
    INPUT_ROW_1 = (By.CSS_SELECTOR, '#row1 input.input-field')
    INSTRUCTIONS_TEXT = (By.ID, 'instructions')

    def page_load(self):
        self.load(self.TEST_URL)

    def click_add_button(self):
        self.bot.click(self.ADD_BUTTON)

    def get_success_message(self):
        self.wait_for_element_visible(self.SUCCESS_MESSAGE)
        return self.bot.element_text(self.SUCCESS_MESSAGE)

    def row_2_exists(self):
        return self.is_element_present(self.ROW_2)

    def write_row_2(self, text):
        assert self.row_2_exists(), 'Row 2 was not found'
        self.bot.clear_and_type(self.INPUT_ROW_2, text)

    def click_save_button(self):
        self.bot.click(self.SAVE_BUTTON)

    def click_edit_button(self):
        self.bot.click(self.EDIT_BUTTON)

    def write_row_1(self, text):
        self.bot.clear_and_type(self.INPUT_ROW_1,text)

    def get_row_1_text(self):
        return self.find_element(self.INPUT_ROW_1).get_attribute('value')

    def instructions_exists(self):
        return self.is_element_present(self.INSTRUCTIONS_TEXT)

