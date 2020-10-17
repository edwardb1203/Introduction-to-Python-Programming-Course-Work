"""2020 hackathon! Schedule hack!"""
authors: "EDWARD BAKER, CHRISTOPHER NGUYEN, GEOFFREY FORSYTHE"
from random import randint
from typing import List, Dict

# GLOBAL VARIABLES
SUBJECT_LIST: List[str] = ["math", "science", "music", "art", "english", "history", "theology", "other"]
HOMEWORK_TYPES: List[str] = ["study", "project", "paper", "problems", "other"]
HOMEWORK_LIST: Dict[str, str] = {}

STUDY_TIME: float = 0.5
PROJECT_TIME: float = 2
PAPER_TIME: float = 1.5
PROBLEM_TIME: float = 0.75
OTHER_TIME: float = 0.5

HOMEWORK_TODAY: List[str] = []

MESSAGE0: str = "Work hard, play hard!"
MESSAGE1: str = "Good luck! You got this!"
MESSAGE2: str = "Get pumped! Give yourself a reward after this!"
MESSAGE3: str = "Make sure to rest your eyes every 20 minutes! Good luck!"
MESSAGE4: str = "Einstein did it. So can you."
MESSAGE5: str = "\"Knowledge is power\" - Someone smart"
MESSAGE6: str = "It's normal to feel stressed, don't forget to relax and reward yourself!"
MESSAGE7: str = "Get some fresh air every now and then!"
MESSAGE8: str = "Reading is food for the brain!"
MESSAGE9: str = "\"Suffer now and live the rest of your life as a champion\" - Muhammad Ali"

MESSAGE_LIST: List[str] = [MESSAGE0, MESSAGE1, MESSAGE2, MESSAGE3, MESSAGE4, MESSAGE5, MESSAGE6, MESSAGE7, MESSAGE8, MESSAGE9]

# MAIN FUNCTION
def main() -> None:
    TIME_REQUIRED: float = 0
    subject: bool = True
    while subject == True:
        
        print("School Subjects: " + str(SUBJECT_LIST))
        question1: str = input("What is your homework subject? ")
        if question1 not in SUBJECT_LIST:
            while question1 not in SUBJECT_LIST:
                print("School Subjects: " + str(SUBJECT_LIST))
                print("Invalid subject type, please choose from list above.")
                question1: str = input("What is your homework subject? ")

        print("Homework Types: " + str(HOMEWORK_TYPES))
        question2: str = input("What is your homework type? ")
        if question2 not in HOMEWORK_TYPES:
            while question2 not in HOMEWORK_TYPES:
                print("Homework Types: " + str(HOMEWORK_TYPES))
                print("Invalid homework type, please choose from list above.")
                question2: str = input("What is your homework type? ")
                
        if question2 == "study":
            TIME_REQUIRED += STUDY_TIME
        elif question2 == "project":
            TIME_REQUIRED += PROJECT_TIME
        elif question2 == "paper":
            TIME_REQUIRED += PAPER_TIME
        elif question2 == "problems":
            TIME_REQUIRED += PROBLEM_TIME
        elif question2 == "other":
            TIME_REQUIRED += OTHER_TIME
            
        HOMEWORK_TODAY.append(question1)
        HOMEWORK_LIST[question1] = question2
        
        question3: str = input("Do you have anymore homework? (yes/no) ")
        if question3 == "no":
            todays_work: int = 0
            subject = False

            print("This is your to-do list for today! " + str(HOMEWORK_LIST))
            print("You should budget out this much time: " + str(TIME_REQUIRED) + " hours!")
            print("Times are based on estimates from NCES.")
            print(MESSAGE_LIST[randint(0,9)])

            for subject in HOMEWORK_TODAY:
                if subject == "math":
                    todays_work += 1
                elif subject == "science":
                    todays_work += 1
            if todays_work > 2:
                print("You should consider splitting up your STEM homework over multiple days to avoid getting overwhelmed!")

if __name__ == "__main__":
    main()