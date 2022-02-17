import pytest

from fractalgebra.helpers import RationalNumber


# Test RationalNumber.as_mixed_fraction method
@pytest.mark.parametrize(
    "num, den, expected",
    [(0, 1, "0"), (3, 2, "1_1/2"), (-1, 2, "-1/2"), (-3, 2, "-1_1/2")],
)
def test_as_mixed_fraction(num, den, expected):
    rn = RationalNumber(numerator=num, denominator=den)
    assert RationalNumber.as_mixed_fraction(rn) == expected
