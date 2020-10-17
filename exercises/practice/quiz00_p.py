"""Practice for our first quiz."""
__author__ = "730312903"

def ayeee(word: str) -> int:
    """Given a string returns thae length of a in it."""
    a_count: int = 0
    i: int = 0
    while i < len(word):
        if word[i] == "a":
            a_count += 1
        i += 1
    return a_count


def ayooo(word1: str, word2: str, word3: str) -> bool:
    """Determines if a word has greater than 10 a's."""
    as_word1: int = ayeee(word1)
    as_word2: int = ayeee(word2)
    as_word3: int = ayeee(word3)
    if as_word1 > 10:
        return True
    if as_word2 > 10:
        return True
    if as_word3 > 10:
        return True
    else:
        return False
    # this is how i did it, which works but the method above is cleaner
    # if as_word1 > 10:
    #     print(True)
    # else:
    #     if as_word2 > 10:
    #         print(True)
    #     else:
    #         if as_word3 > 10:
    #             print(True)
    #         else:
    #             print(False)

    # another alternative method to complete this with just one line of code is
    # return ayeee(word1) > 10 or ayeee(word2) > 10 or ayeee(word3) > 10


def yay_pass_fail(course_grade: float, major: str) -> float:
    """Calculates final grade based off major."""
    pass_grade: int = 60
    final_weight: float
    target_exam_grade: float

    if major == "computer science":
        final_weight = .2
    else:
        if major == "chemistry" or major == "biology":
            final_weight = .2
        else:
            final_weight = .3
    rest_weight: float = 1 - final_weight
    target_exam_grade = (pass_grade - (course_grade * rest_weight)) / final_weight
    return target_exam_grade
    
    # if major == "computer science":
    #     final_exam_weight: float = .2
    # if major == "chemistry" or major == "biology":
    #     final_exam_weight: float = .4
    # else:
    #     final_exam_weight: float = .3
    # needed_grade: float = ((60 - course_grade) * (1.0 - final_exam_weight)) / final_exam_weight
    # print(needed_grade)

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
        






    
