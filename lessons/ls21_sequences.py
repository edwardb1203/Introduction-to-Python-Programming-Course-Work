"""Lesson on sequences."""


from typing import Tuple, List

def main() -> None:
    """Some lists."""
    a_list: List[int] = [110, 210, 211, 301, 311]
    print(a_list)

    i: int = 0 
    while i < len(a_list):
        print(a_list[i])
        i += 1

    names: List[str] = ["Kris", "Kaki", "Ezri"]
    print(names)

    names.append("Edward")
    print(names)

    names1: List[str] = []
    names1.append("Edward")
    names1.append("Kris")
    popped_name: str = names.pop(0)
    print (popped_name)
    #Changes variable at the given index
    names1[0] = "Fart"
    print (names1)





if __name__ == "__main__":
    main()