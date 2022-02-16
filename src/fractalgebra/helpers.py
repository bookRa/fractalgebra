from dataclasses import dataclass
import re
from typing import Callable, ClassVar, Dict, Literal, Optional, Union, List

@dataclass
class RationalNumber:
    numerator: int
    denominator: int

    @classmethod
    # uses the regex to parse a string into a RationalNumber
    def parse_input(cls, input_string: str) -> 'RationalNumber':
        # TODO make better regex that will validate edge cases
        pattern: re.Pattern = re.compile(
            r"^(?P<whole>-?\d+_)?(?P<numer>-?\d+)(?P<denom>/-?\d+)?$gm"
        )
        match: Optional[re.Match] = pattern.match(input_string)
        if match is None:
            # TODO: make this a custom exception
            raise ValueError(f"Invalid input: {input_string}")
        else:
            match_results: Dict[str, Optional[str]] = match.groupdict()
            cls.clean_match_results(match_results)
            clean_results: Dict[str, int] = cls.clean_match_results(match_results)
            return cls.from_mixed_fraction(clean_results)
    
    @classmethod
    # simplifies a RationalNumber with negative values and reduces it to lowest terms
    # TODO: make this an automatic validation when initializing a RationalNumber
    def reduced(cls) -> 'RationalNumber':
        new_n: int = cls.numerator
        new_d: int = cls.denominator
        if new_d == 0:
           raise ZeroDivisionError("Parsing the input revealed a division by zero") 
        if cls.numerator < 0 and cls.denominator < 0:
            new_n, new_d = cls.numerator * -1, cls.denominator * -1
        elif cls.numerator < 0 or cls.denominator < 0:
            new_n, new_d = abs(cls.numerator) * -1, abs(cls.denominator)
        greatest_common_factor: int = cls.gcf(new_n, new_d)
        return cls(new_n // greatest_common_factor, new_d // greatest_common_factor)
    
    @staticmethod
    # uses the Euclidean algorithm to find the greatest common factor of two numbers
    def gcf(x: int, y: int) -> int:
        while y != 0:
            x, y = y, abs(x - y)
        return x


    @staticmethod
    def clean_match_results(match_results: Dict[str, Optional[str]]) -> Dict[str, int]:
        """checks for nonsensical mixed numbers and reformats the results if valid"""
        
        # remove '/' and '_' from raw strings TODO: turn into dict comprehension
        ds: Dict[str, Optional[str]] = {'numer': match_results['numer']}
        if match_results["denom"] is not None:
            ds["denom"] = match_results["denom"][1:]
        if match_results["whole"] is not None:
            ds["whole"] = match_results["whole"][:-1]
        
        int_d: Dict[str, int] = {k: int(v) for k, v in ds.items() if v is not None}
        if len(int_d) == 1: # regex should only allow this if numer was passed
            if 'numer' in int_d:
                int_d = {'whole': int_d['numer']}
            elif 'denom' in int_d:
                raise Exception(f"Unexpected input {str(match_results)}")
        if len(int_d) == 2:
            if 'numer' not in int_d:
                raise InvalidFractionError(str(match_results), "numerator is missing!")
            if 'denom' not in int_d:
                raise InvalidFractionError(str(match_results), "denominator is missing!")
        return int_d

    @staticmethod
    def from_mixed_fraction(mf_dict: Dict[str, int]) -> 'RationalNumber':
        """ensures mixed number doesn't have wonky denominators or negative values"""
        if len(mf_dict) == 1:
            return RationalNumber(mf_dict['whole'], 1)
        whole, numer, denom = mf_dict['whole'], mf_dict['numer'], mf_dict['denom']
        if denom == 0:
            raise ZeroDivisionError("Denominator cannot be zero!")
        if len(mf_dict) == 2:
            return RationalNumber(numer, denom)
        # TODO: possibly allow `whole -numer/-denom` but it's not really standard
        if numer < 0 or denom < 0:
            raise InvalidFractionError(str(mf_dict),
             "mixed fractions can't have a negative fraction part")
        return Calc.add(RationalNumber(whole, 1), RationalNumber(numer, denom))

class Calc:
    """Contains various utilities for fractalgebra"""
    @staticmethod
    def add(a: RationalNumber, b: RationalNumber) -> RationalNumber:
        """adds two rational numbers"""
        return RationalNumber(a.numerator * b.denominator + b.numerator * a.denominator,
                              a.denominator * b.denominator).reduced()

    @staticmethod
    def subtract(a: RationalNumber, b: RationalNumber) -> RationalNumber:
        """subtracts two rational numbers"""
        return Calc.add(a, RationalNumber(-b.numerator, b.denominator))

    @staticmethod
    def multiply(a: RationalNumber, b: RationalNumber) -> RationalNumber:
        """multiplies two rational numbers"""
        return RationalNumber(a.numerator * b.numerator, a.denominator * b.denominator).reduced()
    
    @staticmethod
    def divide(a: RationalNumber, b:RationalNumber) -> RationalNumber:
        """divides two rational numbers"""
        return RationalNumber(a.numerator * b.denominator, a.denominator * b.numerator).reduced()

class Fractalgebra:
    """top-level class for parsing the input string and returning the answer"""

    # TODO: make a fancier typing.Literal type for better validation
    op_dict: Dict[str,
     Callable[
         [RationalNumber,
          RationalNumber],
           RationalNumber]] = {'*': Calc.multiply, '+': Calc.add, '-': Calc.subtract, '/': Calc.divide}
    
    @staticmethod
    # parses the input string
    def parse_length(input_string: str) -> List[str]:
        split_input = input_string.split()
        if len(split_input) <= 2:
            raise InvalidInputError(f"""Input must follow the pattern <fraction>
             <operator> <fraction>, but was {input_string}""")
        return split_input
    
    @staticmethod
    # returns a List[Union[RationalNumber, AllowedOps]];
    # raises InvalidInputError if the input doesn't follow a parseable pattern
    def transform_input(input_list: List[str]) -> List[Union[RationalNumber, str]]:
        transformed: List[Union[RationalNumber, str]] = []
        for i in range(len(input_list)):
            if i % 2 == 0:
                transformed.append(RationalNumber.parse_input(input_list[i]))
            else:
                if input_list[i] not in Fractalgebra.op_dict:
                    raise InvalidInputError(f"""Operator {input_list[i]} is not a valid operator""")
                transformed.append(input_list[i])
        if transformed[-1] in Fractalgebra.op_dict:
            raise InvalidInputError(f"Last argument should be a fraction, not an operator")
        return transformed
    
    @staticmethod
    # reduces the list of rational numbers and operators to a single rational number
    # using order of operations
    def reduce_list(input_list: List[Union[RationalNumber, str]]) -> RationalNumber:
        pemdas: List[str] = ['*', '/', '+', '-']
        updated_list: List[Union[RationalNumber, str]] = input_list.copy()
        for op in pemdas:
            temp_list = updated_list.copy()
            i = 0
            while i<len(temp_list)-1:
                if temp_list[i] == op:
                    prev_rational = temp_list[i-1]
                    next_rational = temp_list[i+1]
                    assert(isinstance(prev_rational, RationalNumber))
                    assert(isinstance(next_rational, RationalNumber))
                    new_rational = Fractalgebra.op_dict[op](prev_rational, next_rational)
                    temp_list = temp_list[:i-1] + [new_rational] + temp_list[i+2:]
                else:
                    i += 1
            updated_list = temp_list.copy()
            if len(updated_list)==1:
                break
        if isinstance(updated_list[0], RationalNumber):
            return updated_list[0]
        else:
            raise Exception("Unexpected error parsing :(")





class InvalidFractionError(Exception):
    """Raised when a fraction is invalid
    Attributes:
        infraction -- the bad thing
        message -- explanation of the error
        suggestion -- a suggestion for how to fix the error
    """

    def __init__(self,
     infraction: Union[int, str],
     message: str,
     suggestion: Optional[str] = None):
        self.infraction = infraction
        self.message = message
        self.suggestion = suggestion
        super().__init__(self.message)

    def __str__(self) -> str:
        base_string = f"{self.message}: {self.infraction}"
        if self.suggestion is not None:
            base_string = f"{base_string} ({self.suggestion})"
        return base_string

class InvalidInputError(Exception):
    """indicates to the user an invalid input"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
    def __str__(self) -> str:
        return self.message