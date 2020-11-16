# """Test for quiz02."""
# __author__ = "730312903"

# import pytest
# from typing import List
# from quiz.quiz02 import caps, abbreviate, phonebook, find_ppl_in_area


# def test_caps_works() -> None:
#     """Test to see if caps works."""
#     assert caps("FatTy") == "FT"


# def test_abbreviate_works() -> None:
#     """Test to see if abbreviate works."""
#     assert abbreviate(["United States of America", "Kris Jordan", "Kaki Ryan Rocks", "Happy BDay"]) == {'United States of America': 'USA','Kris Jordan': 'KJ','Kaki Ryan Rocks': 'KRR','Happy BDay': 'HBD'}


# def test_abbreviate_works_edge() -> None:
#     """Test to see if abbreviate works for edge case."""
#     assert abbreviate([]) == {}


# def test_abbreviate_works_edge_2() -> None:
#     """Test to see if abbreviate works for edge 2nd case."""
#     assert abbreviate(["duke"]) == {"duke": ""}


# def test_phonebook_works() -> None:
#     """Test to see if phonebook works."""
#     assert phonebook([9191919191, 1231231231, 6666666666], ["Fred Brooks", "SittersoN hall", "Phillips Hall"]) == {9191919191: 'FB', 1231231231: 'SN', 6666666666: 'PH'}


# # def test_phonebook_works_edge() -> None:
# #     """Test to see if phonebook works for edge case 1."""
# #     assert phonebook([9191919191, 1231231231, 6666666666, 111122222], ["Fred Brooks", "SittersoN hall", "Phillips Hall"]) == ValueError("Lists must be of the same length!") (WORKS)


# def test_phonebook_works_edge_2() -> None:
#     """Test to see if phonebook works for edge case 2."""
#     assert phonebook([], []) == {}


# def test_phonebook_works_edge_3() -> None:
#     """Test to see if phonebook works for edge case 3."""
#     assert phonebook([9191919191, 1231231231, 6666666666, 11111], ["Fred Brooks", "SittersoN hall", "Phillips Hall", "food"]) == {9191919191: 'FB', 1231231231: 'SN', 6666666666: 'PH'}


# def test_find_ppl_in_area_edge() -> None:
#     assert find_ppl_in_area({9103556789: "SH", 7158423838: "LR", 9106114354: "PB"}, 919) == ["SH", "PB"]



# def test_find_ppl_in_area_edge() -> None:
#     assert find_ppl_in_area({9103556789: "SH", 7158423838: "LR", 9106114354: "PB"}, 347) == []
