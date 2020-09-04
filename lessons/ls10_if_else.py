"""Example of if-then-else statements."""

THE_ANSWER_TO_LIFE_THE_UNIVERSE_AND_EVERYTHING: int = 42

print("Guess a number...")

guess: int = int(input("Your Guess: "))

if guess == THE_ANSWER_TO_LIFE_THE_UNIVERSE_AND_EVERYTHING:
    print("Correct!")
    print("Great work!")
else:
    if guess > THE_ANSWER_TO_LIFE_THE_UNIVERSE_AND_EVERYTHING:
        print("Too high!")
    else:
        print("Too low!")
    print("Incorrect!")
# if guess != THE_ANSWER_TO_LIFE_THE_UNIVERSE_AND_EVERYTHING:
#     print("You know nothing, and that shall cost you everything.")
print("Game over")