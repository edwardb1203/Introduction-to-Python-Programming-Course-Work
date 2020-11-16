from typing import List

poop: List[str] = ["hello", "good", "ok"]

for word in poop:
    print(word)

for i in range(len(poop)):
    poop[i] = (poop[i] + "OK")
print(poop)

