"""An example Python Module."""

from typing import List


def total(xs: List[float]) -> float:
    """Total returns the sum of xs."""
    result: float = 0.0
    # For each x float in xs, add it to result
    for x in xs:
        result += x
    return result

def join(xs: List[int], delimiter: str) -> str:
    """Produce a string where subsequent items are seprated by delim."""
    # for each x float in xs, add delimeter in between
    generated_string: str = ""
    for x in xs:
        if generated_string == "": #dont put delimiter before first item
            generated_string = str(x)
        else:
            generated_string += delimiter + str(x)
    return generated_string

from typing import List

def fill_range(rangestart: int, rangeend: int) -> List[int]:
    """Given two integers, returns range of numbers in btwn."""
    filled_range: List[int] = []
    for number in range(rangestart, rangeend + 1):
        filled_range.append(number)
    return filled_range
