"""Redo of quiz00."""
__author__ = "730312903"
# from exercises.ex04.quiz_redo import
# python -m tools.submission exercises/ex04


def is_tar(tar_heel_word: str) -> bool:
    """Checks word to see if it is made up of a "t" followed by any number of "a" and ending in "r"."""
    i: int = 0
    if tar_heel_word == "":
        return False
    if (tar_heel_word[i] != "t") and (tar_heel_word[i] != "T"):
        return False
    if tar_heel_word[len(tar_heel_word) - 1] != "r" and tar_heel_word[len(tar_heel_word) - 1] != "R":
        return False
    i = 1
    while i < len(tar_heel_word) - 1:
        if tar_heel_word[i] != "a" and tar_heel_word[i] != "A":
            return False
        else:
            i += 1
    return True 


def boot(word: str, number1: int, number2: int) -> str:
    """Given a word/phrase and a range of integers, returns phrase without characters in indicated range."""
    i: int = 0
    new_word: str = ""
    while i < len(word):
        letter: str = word[i]
        if i < number1:
            new_word += letter
        if i > number2:
            new_word += letter
        i = i + 1
    return new_word


def sum_inputs() -> str:
    """User enters numbers, when -1 is entered all numbers all summed."""
    i: int = 0
    total: int = 0
    while i != -1:
        Number: str = input("Enter an int, -1 to sum: ")
        Number2 = (int(Number))
        total += Number2
        total2 = (str(total))
        if Number == "-1":
            total += 1
            total2 = (str(total))
            i = -1
    return "Sum is " + total2
   

def strip(phrase: str, side: str) -> str:
    """Shifts word to indicated side, removing spaces."""
    i: int = 0
    z: int = 0
    new_phrase: str = ""
    if side == "right":
        if phrase[len(phrase) - 1] == " ":
            while i < len(phrase):
                if phrase[len(phrase) - (1 + i)] == " ":
                    i += 1
                else:
                    if phrase[len(phrase) - (1 + i)] != " ":
                        new_phrase = phrase[len(phrase) - (1 + i)] + new_phrase
                        i += 1
        if phrase[len(phrase) - 1] != " ":
            return phrase
        if phrase[z] == " ":
            while (len(phrase) - len(new_phrase)) > z:
                new_phrase = " " + new_phrase
                z += 1
    if side == "left":
        i = 0
        if phrase[i] == " ":
            while i < len(phrase):
                if phrase[i] == " ":
                    i += 1
                else:
                    if phrase[i] != " ":
                        new_phrase = new_phrase + phrase[i]
                        i += 1
        if phrase[0] != " ":
            return phrase
        if phrase[len(phrase) - 1] == " ":
            while (len(phrase) - len(new_phrase)) > z:
                new_phrase = new_phrase + " "
                z += 1
    return new_phrase