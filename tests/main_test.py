import typer
from typer.testing import CliRunner
import pytest

from fractalgebra.main import main

app = typer.Typer()
app.command()(main)

runner = CliRunner()

@pytest.mark.parametrize("input, expected", [
    ("5/2", "2_1/2"),
    ('0', '0'),
    ('', ''),
    ('1/2 * 3_3/4', '1_7/8'),
    ('2_3/8 + 9/8', '3_1/2'),
    ('-1_1/2 + 1_1/2', '0'),
    ('-1_1/2 + -1_1/2', '3'),
])
def test_app(input, expected):
    result = runner.invoke(app, [input])
    assert result.exit_code == 0
    assert result.output == f'= {expected}\n'