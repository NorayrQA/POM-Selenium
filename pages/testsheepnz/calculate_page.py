from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CalculatePage(BasePage):
    calculate_page_url = 'https://testsheepnz.github.io/BasicCalculator.html'
    first_num_locator = (By.ID, 'number1Field')
    second_num_locator = (By.ID, 'number2Field')
    calculate_button_locator = (By.ID, 'calculateButton')
    success_calculate_locator = (By.ID, 'numberAnswerField')
    integer_selector_locator = (By.ID, 'integerSelect')
    select_option_locator = (By.ID, 'selectOperationDropdown')


    def calculate_page_load(self):
        self.load(self.calculate_page_url)

    def click_select_integer_button(self):
        self.bot.click(self.integer_selector_locator)

    def type_first_num(self, first_num):
        self.bot.type(self.first_num_locator, first_num)

    def type_second_num(self, second_num):
        self.bot.type(self.second_num_locator, second_num)

    def select_subtract(self):
        self.bot.select_by_value(self.select_option_locator, '1')

    def click_calculate_button(self):
        self.bot.click(self.calculate_button_locator)

    def get_calculate_answer(self):
        result_text = self.find_element(self.success_calculate_locator).get_attribute('value')
        return result_text

    def calculation_add(self, first_num, second_num):
        self.calculate_page_load()
        self.type_first_num(first_num)
        self.type_second_num(second_num)
        self.click_calculate_button()
        return self.get_calculate_answer()

    def float_add(self, first_num, second_num):
        self.calculate_page_load()
        self.type_first_num(first_num)
        self.type_second_num(second_num)
        self.click_calculate_button()
        return self.get_calculate_answer()

    def subtract_numbers(self, first_num, second_num):
        self.calculate_page_load()
        self.type_first_num(first_num)
        self.type_second_num(second_num)
        self.select_subtract()
        self.click_calculate_button()
        return self.get_calculate_answer()
