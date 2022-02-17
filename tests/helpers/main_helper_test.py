import pytest
from fractalgebra.helpers import Fractalgebra, RationalNumber

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

# Test the Fractalgebra.parse_input method
@pytest.mark.parametrize(
    "input, xnum, xden",
    [("5/2", 5, 2), ("3_2/2", 4, 1), ("-1_1/2", -3, 2), ("0", 0, 1), ("-0", 0, 1)],
)
def test_parse_input(input, xnum, xden):
    rn = Fractalgebra.parse_input(input)
    expected = RationalNumber(numerator=xnum, denominator=xden)
    assert rn == expected