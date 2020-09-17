def time_loop(password: str) -> int:
        """Repeats time loop until password is correct."""
        count: int = 0
        user_input: str
        continue_loop: bool = True
        while continue_loop:
            count += 1
            user_input = input("You are in a time loop, enter the password to get out!")
            if user_input == password:
                continue_loop = False
        return count
        


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

