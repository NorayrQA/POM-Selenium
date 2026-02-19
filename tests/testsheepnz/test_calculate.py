from decimal import Decimal

import pytest
from pages.testsheepnz.calculate_page import CalculatePage
from tests.conftest import driver


class TestCalculate:
    @pytest.mark.parametrize(
        'first_num, second_num, expected',
        [
            pytest.param(5, 7, '12', id='Two_positive_numbers'),
            pytest.param(80, 90, '170', id='Two_big_positive_numbers'),
            pytest.param(-10, 10, '0', id='Negative_and_positive'),
            pytest.param(-5, -5, '-10', id='Two_negative_numbers'),
            pytest.param(0, 0, '0', id='Two_zeros'),
            pytest.param(0.5, 0.5, '1', id='Decimal numbers'),
            pytest.param(999999, 1, '1000000', id='Large_number_boundary'),
            pytest.param('', '', '0', id='Empty_fields'),
        ]
    )
    def test_calculate(self, first_num, second_num, expected, driver):
        calculate_page = CalculatePage(driver)
        calculate_page.calculation_add(first_num, second_num)

        assert calculate_page.get_calculate_answer() == expected

    import pytest

    @pytest.mark.parametrize(
        'first_num, second_num, expected',
        [
            pytest.param(0.1, 0.2, 0.3, id='add_0_1_and_0_2'),
            pytest.param(1.2, 3.4, 4.6, id='add_1_2_and_3_4'),
            pytest.param(2.5, 1.5, 4.0, id='add_2_5_and_1_5'),
            pytest.param(0.75, 0.25, 1.0, id='add_0_75_and_0_25'),
            pytest.param(10.1, 0.2, 10.3, id='add_10_1_and_0_2'),
            pytest.param(5.55, 4.45, 10.0, id='add_5_55_and_4_45'),
            pytest.param(-1.2, 2.3, 1.1, id='add_negative_and_decimal'),
            pytest.param(0.6, 0.6, 1.2, id='add_0_6_and_0_6'),
            pytest.param(3.33, 1.11, 4.44, id='add_3_33_and_1_11'),
        ]
    )
    def test_calculate_float(self, first_num, second_num, expected, driver):
        calculate_page = CalculatePage(driver)
        calculate_page.float_add(first_num, second_num)

        result = float(calculate_page.get_calculate_answer())

        assert result == pytest.approx(expected)

    @pytest.mark.parametrize(
        'first_num, second_num, expected',
        [
            pytest.param(10, 5, '5', id='subtract_10_minus_5'),
            pytest.param(5, 10, '-5', id='subtract_5_minus_10'),
            pytest.param(0, 0, '0', id='subtract_0_minus_0'),
            pytest.param(-5, -5, '0', id='subtract_minus_5_minus_minus_5'),
            pytest.param(-10, 5, '-15', id='subtract_minus_10_minus_5'),
            pytest.param(10, -5, '15', id='subtract_10_minus_minus_5'),
            pytest.param(3.5, 1.5, '2.0', id='subtract_3_5_minus_1_5'),
            pytest.param(1.2, 0.2, '1.0', id='subtract_1_2_minus_0_2'),
            pytest.param(0.5, 1.5, '-1.0', id='subtract_0_5_minus_1_5'),
            pytest.param(10.1, 0.1, '10.0', id='subtract_10_1_minus_0_1'),
        ]
    )
    def test_subtract(self, first_num, second_num, expected, driver):
        calculate_page = CalculatePage(driver)
        calculate_page.subtract_numbers(first_num, second_num)

        actual = Decimal(calculate_page.get_calculate_answer())
        expected = Decimal(expected)

        assert actual == expected

