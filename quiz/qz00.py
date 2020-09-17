"""Responses for quiz00."""
__author__ = "730312903"


def is_tar(tar_heel_word: str) -> bool:
    """Checks word to see if it is made up of a "t" followed by any number of "a" and ending in "r"."""
    i: int = 0
    while i < len(tar_heel_word):
        if tar_heel_word[i] != "t":
            return False
        else:
            i += 1
        if tar_heel_word[i] == "a":
            i += 1
        else:
            if tar_heel_word[i] == "r": 
                return True 
            else:
                return False
    return True 


def boot(word: str, number1: int, number2: int) -> str:
    """Given a word/phrase and a range of integers, returns phrase without characters in indicated range."""
    length_word: int = len(word)
    first_half = range(0, number1)
    second_half = range(number2, len(word))
    modified_word = word[first_half] + word[second_half]
    return modified_word


def sum_inputs() -> str:
    i: int = 0
    Number: int = input("Enter an int, -1 to sum: ")
    while i != -1:
        Number: int = input("Enter an int, -1 to sum: ")
        Total: int = Number += Number
        if Number == -1:
            i = -1
    return Total

def strip(phrase: str, side: str) -> str:
    """Shifts word to indicated side."""
    i: int = 0
    while i < len(phrase)
        if side == "left"
            if phrase[i] == " ":
                new_phrase = phrase[i + 1] - " "
        if side == "right"
            if phrase[i] == " ":
                new_phrase = phrase[i - 1] - " "
    return new_phrase



