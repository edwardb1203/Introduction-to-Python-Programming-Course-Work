"""This is an exercise to reverse engineer algorithms."""
__author__ = "730312903"

from typing import List


def count(number_list: List[int], specific_number: int) -> int:
    """Given a list of numbers and a specific number, checks list for occurrences of given number."""
    # Iterate through a list
    # Keep track of total number of occurrences
    total_occurrences: int = 0
    for number in number_list:
        if number == specific_number:
            total_occurrences += 1
    return total_occurrences


def all(number_list: List[int], specific_number: int) -> bool:
    """Given a list and a specific number, checks list to see if all numbers match given."""
    # Iterate through a list
    # Check to see if numbers match given using if statement
    # If match then return true
    if number_list == []:
        return False
    for number in number_list:
        if number != specific_number:
            return False
    return True


def max(number_list: List[int]) -> int:
    """Given a list of ints, returns the largest #."""
    # iterate through a list
    # find the largest value and return it
    i: int = 0
    # if len(input) == i:
    # raise ValueError("max() arg is an empty List")
    max_number = number_list[i]
    for number in number_list:
        if number > max_number:
            max_number = number
    return max_number


def is_equal(number_list1: List[int], number_list2: List[int]) -> bool:
    """Checks to see if two lists are equal."""
    if len(number_list1) != len(number_list2):
        return False
    elif number_list1 == number_list2:
        return True
    elif number_list1 != number_list2:
        return False
    return True


def concat(number_list1: List[int], number_list2: List[int]) -> List[int]:
    """Given two lists, joins them together."""
    joined_list: List[int] = []
    for numbers in number_list1:
        joined_list.append(numbers)
    for numbers in number_list2:
        joined_list.append(numbers)
    return joined_list


def sub(number_list: List[int], start_index: int, end_index: int) -> List[int]:
    """Given a list and two indices, returns list btwn indices."""
    indexed_list: List[int] = []
    if start_index == len(number_list):
        return indexed_list
    if start_index < 0:
        start_index = 0
    for numbers in number_list:
        if numbers == number_list[start_index]:
            while start_index < end_index + 1:
                indexed_list.append(numbers)
                start_index += 1
                break
        if start_index == end_index:
            return indexed_list
    return indexed_list


def splice(number_list11: List[int], index: int, number_list22: List[int]) -> List[int]:
    """Given two lists and an indice, splices second list into the first."""
    indexed_list: List[int] = []
    i: int = 0
    if index < 0:
        indexed_list = concat(number_list22, number_list11)
        return indexed_list
    if index > len(number_list11):
        indexed_list = concat(number_list11, number_list22)
        return indexed_list
    else:
        while i < index:
            indexed_list.append(number_list11[i])
            i += 1
        for numbers in number_list22:
            indexed_list.append(numbers)
        while i < len(number_list11):
            indexed_list.append(number_list11[i])
            i += 1
        return indexed_list