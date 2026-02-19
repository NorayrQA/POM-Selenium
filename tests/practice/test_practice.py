from pages.practice.practice_page import RowPage
from tests.conftest import driver


class TestException:
    def test_case_1_no_such_element_exception(self, driver):
        row_page = RowPage(driver)
        row_page.page_load()
        row_page.click_add_button()

        assert row_page.get_success_message() == 'Row 2 was added'
        assert row_page.row_2_exists(), 'Row 2 was not found'

    def test_case_2_element_not_interactable_exception(self, driver):
        row_page = RowPage(driver)
        row_page.page_load()
        row_page.click_add_button()
        row_page.write_row_2('pizza 2')
        row_page.click_save_button()

        assert row_page.get_success_message() == 'Row 2 was saved'
        assert row_page.row_2_exists(), 'Row 2 was not found'

    def test_case_3_invalid_element_state_exception(self, driver):
        row_page = RowPage(driver)
        row_page.page_load()
        row_page.click_edit_button()
        row_page.write_row_1('pizza 3')

        assert row_page.get_row_1_text() == 'pizza 3'

    def test_case_4_stale_element_reference_exception(self, driver):
        row_page = RowPage(driver)
        row_page.page_load()

        assert row_page.instructions_exists(), 'Instructions text not found'

        row_page.click_add_button()

        assert not row_page.instructions_exists(), 'Instructions text should be removed'

