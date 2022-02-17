from fractions import Fraction as frac

import hypothesis.strategies as st
import pytest
from hypothesis import Verbosity, given, settings

from fractalgebra.helpers import Calc, Fractalgebra, RationalNumber


# Test the RationalNumber.parse_input method
@pytest.mark.parametrize(
    "input, xnum, xden",
    [("5/2", 5, 2), ("3_2/2", 4, 1), ("-1_1/2", -3, 2), ("0", 0, 1), ("-0", 0, 1)],
)
def test_parse_input(input, xnum, xden):
    rn = RationalNumber.parse_input(input)
    expected = RationalNumber(numerator=xnum, denominator=xden)
    assert rn == expected


# Test RationalNumber.as_mixed_fraction method
@pytest.mark.parametrize(
    "num, den, expected",
    [(0, 1, "0"), (3, 2, "1_1/2"), (-1, 2, "-1/2"), (-3, 2, "-1_1/2")],
)
def test_as_mixed_fraction(num, den, expected):
    rn = RationalNumber(numerator=num, denominator=den)
    assert RationalNumber.as_mixed_fraction(rn) == expected


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


# Test the Fractalgebra.transform_input method
@pytest.mark.parametrize(
    "input, expected",
    [
        (["0"], [RationalNumber(numerator=0, denominator=1)]),
        (
            ["1/2", "+", "1/2"],
            [
                RationalNumber(numerator=1, denominator=2),
                "+",
                RationalNumber(numerator=1, denominator=2),
            ],
        ),
    ],
)
def test_transform_input(input, expected):
    assert Fractalgebra.transform_input(input) == expected


# TODO: property-based testing (hypothesis)
