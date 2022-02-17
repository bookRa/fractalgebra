import typer
from typer.testing import CliRunner

from fractalgebra.main import main

app = typer.Typer()
app.command()(main)

runner = CliRunner()

def test_app():
    result = runner.invoke(app, ['0'])
    assert result.exit_code == 0
    assert result.output == '= 0\n'