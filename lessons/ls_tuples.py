"""Examples of Sequences."""

from typing import Tuple


Color = Tuple[int, int, int]


def brighter(a_color: Color) -> Color:
    """Return a new tuple that is lsightly brighter!"""
    red: int = int(a_color[0] * 1.1)
    green: int = int(a_color[1] * 1.1)
    blue: int = int(a_color[2] * 1.1)
    return (red, green, blue)

