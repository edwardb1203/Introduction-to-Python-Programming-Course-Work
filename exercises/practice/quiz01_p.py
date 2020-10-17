"""Quiz 01 practice."""
__author__ = "730312903"

from typing import List


def orderPrice(order: List[str], menu: List[str], price: List[float]) -> float:
    final_price: float = 0

    for item in order:
        in_menu: bool = False

        for i in range(len(menu)):
            if item == menu[i]:
                final_price += price[i]
                in_menu = True
        if not in_menu:
            final_price += 2.0

    return final_price


def sortScore(scores: List[int]) -> List[int]:
    sorted: List[int] = []
    length = range(len(scores))

    for i in length:
        min_index: int = 0

        for j in range(len(scores))
        if scores[j] < scores[min_index]:
            min_index = j
        sorted.append(score[min_index])
        scores.pop(min_index)



    return sorted




def noDupes(number_list: List[int]) -> List[int]:
    """Given a list of ints, returns without any dupes."""
    new_list: List[int] = [number_list[0], ]
    i: int = 1
    for numbers in number_list:
        if numbers != number_list[i]:
            new_list.append(numbers)
            i += 1
    return new_list