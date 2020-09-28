"""Testing for functionality of utils."""
__author__ = "730312903"

import pytest
from exercises.ex05.utils import count, all, max, is_equal, concat, sub, splice
from typing import List


def test_count_one() -> None:
    """Test counting a single instance of the needle in the haystack."""
    assert count([1, 1, 0, 1, 20, 100], 0) == 1


def test_count_none() -> None:
    """Test counting no instance of variable."""
    assert count([1, 1, 2, 1, 20, 100], 0) == 0


def test_count_multi() -> None:
    """Test counting multi instance of variable."""
    assert count([1, 0, 0, 1, 0, 100], 0) == 3


def test_all_none() -> None:
    """Test for no instances, results in false."""
    assert not all([0, 0, 0], 1)


def test_all_alls() -> None:
    """Tests for all matches, results in true."""
    assert all([1, 1, 1], 1)


def test_all_one() -> None:
    """Tests for one match, results in false."""
    assert not all([1, 0, 0], 1)


def test_all_few() -> None:
    """Test for a few matches, results in false."""
    assert not all([0, 0, 1, 0, 1, 1, 1, 0, 0, 0], 1)


def test_all_empty() -> None:
    """Test for an empty list, should be false."""
    assert not all([], 1)


# def test_max_of_empty() -> None:
#     """Calling the `max` function with an empty List should raise a Value Error."""
#     with pytest.raises(ValueError):
#         empty_list: List[int] = []
#         max(empty_list)


def test_max_order() -> None:
    """Tests to see if fucntion works for ordered list."""
    assert max([1, 2, 3, 4, 5, 6, 7]) == 7


def test_max_chaos() -> None:
    """Tests to see if fucntion works for chaos list."""
    assert max([1, 3, 7, 1, 3, 2, 4]) == 7


def test_max_neg() -> None:
    """Tests to see if fucntion works for negative in list + chaos."""
    assert max([1, -3, 7, 1, -3, 2, -4]) == 7


def test_is_equal_normal() -> None:
    """Test for two equal lists."""
    assert is_equal([1, 0, 1], [1, 0, 1]) 


def test_is_equal_false() -> None:
    """Test for two non equal lists."""
    assert not is_equal([1, 0, 1], [2, 0, 1])


def test_is_equal_neg() -> None:
    """Test for two same len but neg lists."""
    assert not is_equal([1, 0, 1], [-1, 0, -1])


def test_is_equal_empty() -> None:
    """Test for two empty lists."""
    assert is_equal([], [])


def test_is_equal_diff_len() -> None:
    """Test for two diff length lists."""
    assert not is_equal([1, 0, 1], [1, 0, 1, 1, 0])


def test_concat_equal() -> None:
    """Attempts to concat two lists of equal length."""
    assert concat([1, 0, 2], [3, 5, 7]) == [1, 0, 2, 3, 5, 7]


def test_concat_diff() -> None:
    """Attempts to concat two lists of diff length."""
    assert concat([1, 0, 2], [3, 5, 7, 5]) == [1, 0, 2, 3, 5, 7, 5]


def test_concat_empty() -> None:
    """Attempts to concat two lists of empty length."""
    assert concat([], []) == []


def test_sub_works() -> None:
    """Should return list between two indices."""
    assert sub([1, 7, 9, 3, 8, 5], 2, 5) == [9, 3, 8]


def test_sub_neg() -> None:
    """Should start from beginning of list."""
    assert sub([1, 7, 9, 3, 8, 5], -2, 2) == [1, 7]


def test_splice_works() -> None:
    """Should return list splice into list."""
    assert splice([7, 5, 4, 9], 1, [0, 1]) == [7, 0, 1, 5, 4, 9]


def test_splice_neg() -> None:
    """Should return list splice into list negative."""
    assert splice([7, 5, 4], -1, [0, 1, 2]) == [0, 1, 2, 7, 5, 4]


def test_splice_empty() -> None:
    """Splice a list into an empty list."""
    assert splice([7, 5, 4], 1, []) == [7, 5, 4]


def test_splice_empty_2() -> None:
    """Tries to splice into empty first list."""
    assert splice([], 1, [1, 4, 8]) == [1, 4, 8]


def test_splice_greater() -> None:
    """Splice second list onto end."""
    assert splice([7, 5, 4, 8], 6, [0, 1]) == [7, 5, 4, 8, 0, 1]