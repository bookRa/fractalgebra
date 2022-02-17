import typer

from fractalgebra.helpers import Fractalgebra

helpstring = """two or more rational numbers (e.g. 2/3, -2/3, 1_1/2, -1_1/2, 5)
separated by a spaces and an operator (one of +, -, *, or /)
        e.g: 8 * 1/2 - -18/3 / -1_10/5
    = 1
    
** note that mixed number with a negative fraction (e.g. 4_-1/2) is NOT a rational number
    """

def main(input: str = typer.Argument(..., help = helpstring)):
    """
    Perform basic arithmatic on two or more fractions (or mixed number)
    using the pattern <fraction> <operator> <fraction> <operator> <fraction>
        
    """
    try:
        fractalgebra_answer: str = Fractalgebra.solve(input)
        typer.echo(f"= {fractalgebra_answer}")
    except Exception as e:
        typer.echo("There was a problem solving your problem :(")
        typer.echo(e)

if __name__ == "__main__":
    typer.run(main) 
