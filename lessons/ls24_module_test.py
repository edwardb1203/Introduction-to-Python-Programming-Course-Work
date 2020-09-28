"""An example of a test module in pytest."""

from lessons.ls24_module import total, join, fill_range
from typing import List


def test_total_empty() -> None:
    """Total of empty list should be 0.0."""
    assert total([]) == 0.0

def test_total_single_item() -> None:
    """Total of a single item list should be the fisrt item's value."""
    assert total([110.0]) == 110.0

def test_total_many_items() -> None:
    """Total of a list with many items should be their sum."""
    assert total([1.0, 2.0, 3.0]) == 6.0

def test_join_use_case() -> None:
    assert join([1, 2, 3], ", ") == "1, 2, 3"


def test_join_edge_single_item() -> None:
    assert join([1], ", ") == "1"

def test_join_edge_empty_delimiter() -> None:
    assert join([1, 2, 3], "") == "123"


def test_fill_range_use_0() -> None:
    low: int = 1
    high: int = 3
    expected_result: List[int] = [1, 2, 3]
    assert fill_range(low, high) == expected_result

def test_fill_range_use_0() -> None:
    low: int = -7
    high: int = -4
    expected_result: List[int] = [-7, -6, -5, -4]
    assert fill_range(low, high) == expected_result


def test_fill_range_use_0() -> None:
    low: int = -4
    high: int = 0
    expected_result: List[int] = [-4, -3, -2, -1, 0]
    assert fill_range(low, high) == expected_result


def test_fill_range_use_1() -> None:
    low: int = 1 
    high: int = 1
    expected_result: List[int] = [1]
    assert fill_range(low, high) == expected_result

def test_fill_range_use_1() -> None:
    high: int = 1 
    low: int = 1
    expected_result: List[int] = [1]
    assert fill_range(low, high) == expected_result




