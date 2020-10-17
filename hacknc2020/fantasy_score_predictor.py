from random import randint

team1: str = input("What is team #1? ")
team2: str = input("What is team #2? ")
Score_1: int = (randint(0,100))
Score_2: int = (randint(0,100))

if team1 == "redefininggodtier":
    Score_1 = 9000
if Score_1 < Score_2:
    print(team1 + " loses: " + str(Score_1) + " " + team2 + " wins!: " + str(Score_2))
    print(team1 + " YOU SUCK AT FANTASY!")
if Score_1 > Score_2:
    print(team1 + " wins!: " + str(Score_1) + " " + team2 + " loses!: " + str(Score_2))
    print(team2 + " YOU SUCK AT FANTASY!")
