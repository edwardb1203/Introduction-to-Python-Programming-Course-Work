"""For loops."""

name: str = "Edward"
for character in name:
    print(character)

for i in range(1, 20, 2):
    print(i)

from typing import List
names: List[str] = ["Edward", "Chris", "Aiden"]
for item in names:
    print("hello, " + item)

message: str = ""

for i in range(1,3):
    message += "h"
    for h in range(0, i):
        message += "e"