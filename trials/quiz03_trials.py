from __future__ import annotations
from typing import Optional

# """Trials for quiz03."""



# def main() -> None:
#     person2 = Person("Aiden", person1)
#     person1 = Person("edward", person2)

#     print(person1)


# class Person:
#     name: str
#     boss: Person

#     def __init__(self, name: str, boss: Person):
#         self.name = name
#         self.boss = boss


# if __name__ == "__main__":
#     main()

class Box: 
    x: int = 1 

    def inc_b(self) -> Box:
        b: Box = Box()
        self.x += 1
        b.x = self.x
        b.x += 1
        return b
    
    def inc_c(self) -> Box:
        self.x += 1
        return self
    
    def add(self, other: Box) -> int:
        self.x += other.x
        return self.x

def main() -> None:
    a: Box = Box()
    b: Box = a.inc_b()
    c: Box = b.inc_c()
    print(c.add(c))

if __name__ == "__main__":
     main()


