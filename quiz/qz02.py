"""Responses for Quiz 02."""
__author__ = "730312903"

from typing import List, Dict


def abbreviate(names: List[str]) -> Dict[str, str]:
    """Given a list of names, produces dictionary with abbreviations of capitalized letters."""
    abbrev_dict: Dict[str, str] = {}
    for word in names:
        abbrev_dict[word] = caps(word)
    return abbrev_dict


def caps(word: str) -> str:
    """Takes a word and returns only the capitalized letters."""
    capped_word: str = ""
    for letters in word:
        if letters.isupper():
            capped_word += letters
    return capped_word


def phonebook(pnumbers: List[int], owners: List[str]) -> Dict[int, str]:
    """Given phone numbers and owners, returns dictionary with proper matchups and abbrev names."""
    if len(pnumbers) != len(owners):
        raise ValueError("Lists must be of the same length!")
    owners_dict: Dict[str, str] = abbreviate(owners)
    phonebook: Dict[int, str] = {}
    i: int = 0
    for number in pnumbers:
        if owners_dict[owners[i]] == "":
            i += 1
            break
        phonebook[number] = owners_dict[owners[i]]
        i += 1
    return phonebook


def find_ppl_in_area(num_map: Dict[int, str], code: int) -> List[str]:
    """Finds people initials whose area code matche input code."""
    if len(str(code)) != 3:
        raise ValueError("Area code must be 3 digits!")
    people_in_area: List[str] = []
    for number in num_map:
        new_num = str(number)
        if (new_num[0:3]) == str(code):
            people_in_area.append(num_map[number])
    return people_in_area