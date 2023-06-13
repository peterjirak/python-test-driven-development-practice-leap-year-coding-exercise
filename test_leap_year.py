import pytest

from leap_year import leap_year

def test_can_invoke_leap_year_function():
    leap_year(1)

def test_leap_year_function_returns_false_for_years_not_divisible_by_four():
    assert leap_year(1983) == False

def test_leap_year_function_returns_true_for_divisible_by_four_but_not_100_or_400():
    assert leap_year(1984) == True

def test_returns_false_for_divisible_by_4_and_divisible_by_100_but_not_400():
    assert leap_year(1900) == False
    