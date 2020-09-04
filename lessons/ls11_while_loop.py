"""An example of a while loop statement!"""

iterations: int = int(input("How many times?"))
# iterations tells us how many times we will try this loop
i: int = 0 

while i < iterations:
    if i % 1000 == 0:
        print("In repeat block!")
        print("i is " + str(i))
    i = i + 1

print("after repeat block! i is " + str(i))
