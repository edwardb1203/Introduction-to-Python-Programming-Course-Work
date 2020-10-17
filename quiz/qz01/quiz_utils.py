"""Responses for quiz01."""
__author__ = "730312903"


from typing import List


def strs_to_floats(word_list: List[str]) -> List[float]:
    """Given a list of strings, returns them as floats."""
    float_list: List[float] = []
    for words in word_list:
        word: float = float(words)
        float_list.append(word)
    return float_list


def lookup(labels: List[str], values: List[float], desired: str) -> float:
    """Looks up value of desired item."""
    if len(labels) != len(values):
        raise ValueError("Lists must be of equal length!")

    value_of_desired: float = 0
    for name in labels:
        in_labels: bool = False
       
        for i in range(len(values)):
            if desired == labels[i]:
                value_of_desired += values[i]
                in_labels = True
        if not in_labels:
            raise ValueError("Desired not in labels!")
        return value_of_desired
    return value_of_desired


def undelimit(words: str) -> List[str]:
    """Given a string delimited with commas, returns a list undelimited."""
    undelim_list: List[str] = []
    new_word: str = ""
    i: int = 0
    while i < len(words):
        letter: str = words[i]
        if letter != ",":
            new_word += letter
            i += 1
        else:
            undelim_list.append(new_word)
            new_word = ""
            i += 1
    if i == len(words):
        undelim_list.append(new_word)
    return undelim_list


def avg_column(data: List[str], column_name: str) -> float:
    """Given a list of data columns, returns the mean of all values in specified column."""
    # honestly I am very tired and don't have the brain capacity to code properly anymore, so I will try put most of my
    # ideas into pseduo code
    # I know that we should use a nested for loop to be able to go across and down each column
    # I know that we should use our strs_to_floats function to obviously convert our str data
    # to floats so that we can perform operations on it and get the mean
    # I know we should also use lookup to put us in the right column, "high" , "low", etc
    desired_avg: float = 0
    if column_name == "":
        raise ValueError("Need column name!")
    # if column_name == "high":
    #     strs_to_floats(data)
    #     for i in data:
    #         for j in range(len(data))
    #             lookup(high)
    #     # avg = nums in column added / 4
    #     desired_avg += avg
    # if column_name == "low":
    #     strs_to_floats(data)
    #      for i in data:
    #         for j in range(len(data))
    #             lookup(low)
    #     # avg = nums in column added / 4
    #     desired_avg += avg
    # if column_name == "precipitation":
    #     strs_to_floats(data)
    #      for i in data:
    #         for j in range(len(data))
    #             lookup(preciptation)
    #     # avg = nums in column added / 4
    #     desired avg += avg
    return desired_avg