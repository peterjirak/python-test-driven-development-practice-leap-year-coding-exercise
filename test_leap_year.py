import pytest

from leap_year import leap_year

def test_can_invoke_leap_year_function():
    leap_year(1)

def test_leap_year_function_returns_false_for_years_not_divisible_by_four():
    assert leap_year(1983) == False
