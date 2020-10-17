"""Tests for quiz01."""
__author__ = "730312903"

import pytest
from typing import List
from quiz.qz01.quiz_utils import strs_to_floats, lookup, undelimit


def test_strs_to_floats_works() -> None:
    """Test to make sure a list of strings returns as floats."""
    assert strs_to_floats(["1.1", "9.0", "3.4"]) == [1.1, 9.0, 3.4]


def test_strs_to_floats_empty() -> None:
    """Test to see what happens with empty list."""
    assert strs_to_floats([]) == []


def test_strs_to_floats_works_multipled() -> None:
    """Test to make sure a list of strings returns as floats with multiple decimals."""
    assert strs_to_floats(["1.11111", "9.0212", "3.4232"]) == [1.11111, 9.0212, 3.4232]


def test_lookup_works() -> None:
    """Test to see if given a listed name, the function returns its float value."""
    assert lookup(["pi", "e", "origin"], [3.14, 2.72, 0.0], "pi") == 3.14

def test_lookup_works_2nd() -> None:
    """Test to see if given a listed name at third spot, the function returns its float value."""
    assert lookup(["pi", "e", "origin"], [3.14, 2.72, 0.0], "origin") == 0.0


def test_lookup_works_value1() -> None:
    """Test to see if 1st value error is raised."""
    with pytest.raises(ValueError):
        lookup(["pi", "e", "origin"], [3.14, 2.72, 0.0, 1.1], "origin")
    

def test_lookup_works_value2() -> None:
    """Test to see if 2nd value error is raised."""
    with pytest.raises(ValueError):
        lookup(["pi", "e", "origin"], [3.14, 2.72, 0.0], "carolina")


def test_undelimit_works() -> None:
    """Test to see if undelimit puts strin in list seperate by commas."""
    assert undelimit("one,two,three") == ["one", "two", "three"]


def test_undelimit_just_commas() -> None:
    """Test to see if properly implemented when given only commas."""
    assert undelimit(",,") == ["","",""]


data: List[str] =  ["high,low, precipitation",
        "81.0,53.0,0.1",
        "70.0,52.0,0.1",
        "77.0,54.0,0.1",
        "6..0,44.0,0.1",
]


def test_avg_column_high() -> None:
    """Tests to see if function works given high."""
    avg_column(data, "high") == 73.5


def test_avg_column_low() -> None:
    """Tests to see if function works given low."""
    avg_column(data, "low") == 50.75


def test_avg_column_precipitation() -> None:
    """Tests to see if function works given precipitation."""
    avg_column(data, "precipitation") == 0.1