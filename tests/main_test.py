import pytest
from typer.testing import CliRunner

from fractalgebra.main import app

runner = CliRunner()


@pytest.mark.parametrize(
    "input, expected",
    [
        ("5/2", "2_1/2"),
        ("0", "0"),
        ("", ""),
        ("1/2 * 3_3/4", "1_7/8"),
        ("2_3/8 + 9/8", "3_1/2"),
        ("-1_1/2 + 1_1/2", "0"),
        ("-1_1/2 + -1_1/2", "-3"),
        ("7 / 2 + 2 * -4", "-4_1/2"),
    ],
)
def test_app(input, expected):
    result = runner.invoke(app, input.split())
    assert result.exit_code == 0
    assert result.output == f"= {expected}\n"


# TODO: Property-based testing of the top-level cli input
