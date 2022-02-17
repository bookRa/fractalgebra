import pytest
from fractalgebra.helpers import RationalNumber, Calc

# Test the Calc.add method
@pytest.mark.parametrize(
    "num1, den1, num2, den2, num_expected, den_expected",
    [
        (1, 2, 1, 2, 1, 1),
        (0, 1, 0, 1, 0, 1),
        (1, 2, 1, 3, 5, 6),
    ],
)
def test_add_rationals(num1, den1, num2, den2, num_expected, den_expected):
    test_a = RationalNumber(numerator=num1, denominator=den1)
    test_b = RationalNumber(numerator=num2, denominator=den2)
    expected_ans = RationalNumber(numerator=num_expected, denominator=den_expected)
    assert Calc.add(test_a, test_b) == expected_ans

