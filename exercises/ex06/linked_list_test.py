"""Tests for linked list utils."""


from exercises.ex06.linked_list import Node, last, value_at, max, linkify, is_equal, scale, concat, sub, splice

__author__ = "730312903"


def test_last_empty() -> None:
    """Last of an empty List should be the empty list."""
    assert last(None) is None


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_last_one_value() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, None)
    assert last(linked_list) == 1


def test_value_at_zero() -> None:
    """Testing for index at 0."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 0) == 1


def test_value_at_empty() -> None:
    """Testing for an empty list."""
    assert value_at(None, 1) is None


def test_value_at_exists() -> None:
    """Testing an existing index."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 2) == 3


def test_value_at_nonexists() -> None:
    """Testing an non-existant index."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 4) is None


def test_max_works() -> None:
    """Test to see if max fucntion will find hte max in a linked list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_max_works_outorder() -> None:
    """Test to see if max fucntion will find hte max in a linked list out of order."""
    linked_list = Node(2, Node(3, Node(1, None)))
    assert max(linked_list) == 3


def test_max_works_none() -> None:
    """Test to see if max function returns none for empty list."""
    assert max(None) is None


def test_linkify_works() -> None:
    """Test to see if linkify works as intended."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert is_equal(linked_list, linkify([1, 2, 3]))


def test_linkify_works_none() -> None:
    """Test to see if linkify works as intended for none."""
    assert linkify([]) is None


def test_linkify_works_one() -> None:
    """Test to see if linkify works as intended for one."""
    linked_list = Node(1, None)
    assert is_equal(linked_list, linkify([1]))


def test_scale_works() -> None:
    """Test to see if scale works as intended."""
    linked_list = Node(2, Node(4, Node(6, None)))
    assert is_equal(scale(linkify([1, 2, 3]), 2), linked_list)


def test_scale_works_none() -> None:
    """Test to see if scale works as intended for none."""
    assert is_equal(scale(linkify([]), 2), None)


def test_scale_works_zero() -> None:
    """Test to see if scale works for a factor of 0."""
    linked_list = Node(0, Node(0, Node(0, None)))
    assert is_equal(scale(linkify([1, 2, 3]), 0), linked_list)


def test_concat_works() -> None:
    """Test to see if concat works as intended."""
    linked_list = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    assert is_equal(concat(linkify([1, 2, 3]), linkify([4, 5])), linked_list)


def test_concat_no_lhs() -> None:
    """Test to see if concat works as intended."""
    linked_list = Node(4, Node(5, None))
    assert is_equal(concat(linkify([]), linkify([4, 5])), linked_list)


def test_concat_no_rhs() -> None:
    """Test to see if concat works as intended."""
    linked_list = Node(4, Node(5, None))
    assert is_equal(concat(linkify([4, 5]), linkify([])), linked_list)


def test_sub_works() -> None:
    """Test to see if sub works as intended."""
    linked_list = Node(2, Node(3, None))
    assert is_equal((sub(linkify([1, 2, 3, 4]), 1, 2)), linked_list)


def test_sub_works_greaterstart() -> None:
    """Test to see if sub works as intended when start greaer than length."""
    assert is_equal((sub(linkify([1, 2, 3, 4]), 5, 2)), None)


def test_sub_works_negativestart() -> None:
    """Test to see if sub works as intended with a negative start."""
    linked_list = Node(1, Node(2, None))
    assert is_equal((sub(linkify([1, 2, 3, 4]), -1, 2)), linked_list)


def test_splice_works() -> None:
    """Test to see if splice works as intended."""
    linked_list = Node(1, Node(3, Node(4, Node(2, None))))
    assert is_equal(splice(linkify([1, 2]), 1, linkify([3, 4])), linked_list)


def test_splice_works_greater() -> None:
    """Test to see if splice works with a larger index then list len."""
    linked_list = Node(1, Node(2, Node(3, Node(4, None))))
    assert is_equal(splice(linkify([1, 2]), 3, linkify([3, 4])), linked_list)


def test_splice_negative() -> None:
    """Test to see if splice works as intended for negative index."""
    linked_list = Node(3, Node(4, Node(1, Node(2, None))))
    assert is_equal(splice(linkify([1, 2]), -1, linkify([3, 4])), linked_list)