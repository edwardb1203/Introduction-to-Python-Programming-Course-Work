"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional, List

__author__ = "730312903"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        """Produce a string representation of a linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> Optional[int]:
    """Returns the last value of a Linked List, or None if the list is empty."""
    if head is None:
        return None
    if head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> Optional[int]:
    """Returns value of Node at the given index."""
    if head is None:
        return None
    if index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> Optional[int]:
    """Given a Node, returns the max value in the list."""
    if head is None:
        return None
    elif head.next is None:
        return head.data
    else:
        maximum = max(head.next)
        if maximum is None:
            return head.data
        else:
            if head.data <= maximum:
                return maximum
            else:    
                return head.data


def linkify(values: List[int]) -> Optional[Node]:
    """Given a list of values, returns a linked list of nodes."""
    if len(values) == 0:
        return None
    else:
        return Node(values[0], linkify(values[1:]))
      

def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Given a node and a scaler, scales data in node."""
    if head is None:
        return None
    if head.next is None:
        return Node((head.data) * factor, scale((head.next), factor))
    else:
        return Node((head.data) * factor, scale((head.next), factor))

    
def concat(lhs: Optional[Node], rhs: Optional[Node]) -> Optional[Node]:
    """Given two linked lists, concats them."""
    if lhs is None and rhs is None:
        return None
    if lhs is None and rhs is not None:
        n2 = Node(rhs.data, concat(lhs, rhs.next))
        return n2
    else:
        if lhs is not None:
            n1 = Node(lhs.data, concat(lhs.next, rhs))
            return n1
    return None


def sub(liist: Optional[Node], start: int, length: int) -> Optional[Node]:
    """Given a linked list and start index with length, returns subset of linked list."""
    if liist is None:
        return None
    elif start > length:
        return None
    elif start < 0:
        start = 0
        return sub(liist, start, length)
    elif length == 0:
        return Node(liist.data, None)
    else:
        if start > 0:
            return sub(liist.next, start - 1, length)
        elif start == 0:
            return Node(liist.data, sub(liist.next, start, length - 2))
    return liist


def splice(list_a: Optional[Node], index: int, list_b: Optional[Node]) -> Optional[Node]:
    """Given two linked lists and an index, splices them together at index."""
    if list_a is None:
        return list_b
    elif list_b is None:
        return list_a
    elif list_a is None and list_b is None:
        return None
    if index <= 0:
        return concat(list_b, list_a)
    else:
        return Node(list_a.data, splice(list_a.next, index - 1, list_b))
    

# def seq(lo: int, hi: int) -> Optional[Node]:
#     """Return sequence of nodes between lo and hi, not inclusive of hi."""
#     if lo >= hi:
#         return None
#     else:
#         subproblem: int = lo
#         rest: Optional[Node] = seq(lo + 1, hi)
#         return Node(subproblem, rest)

# def includes(haystack: Optional[Node], needle: int) -> bool:
#     """Is needle in the haystack?"""
#     if haystack == None:
#         return False
#     elif haystack.data == needle:
#         return True
#     else:
#         return includes(haystack.next, needle)

# start_node = sub(list_a, 0, index)
# middle_node = concat(start_node, list_b)
# end_node = sub(list_a, index, 100000000)
# spliced_node = concat(middle_node, end_node)
# return spliced_node