"""Demonstration of a recursive data structure!"""

from __future__ import annotations
from typing import Optional


class Node:
    data: int
    next: Optional[Node] 

    def __init__(self, data: int, next: Optional[Node]):
        self.data = data
        self.next = next


def count(a_node: Optional[Node]) -> int:
    if a_node == None:
        return 0
    else:
        return 1 + count(a_node.next)

print(None)

head: Node = Node(210, None)
print(count(head))

head = Node(110, head)
print(count(head))

head = Node(101, head)
print(count(head))

# Always check if list is empty, this is the base case (we check if head is none)