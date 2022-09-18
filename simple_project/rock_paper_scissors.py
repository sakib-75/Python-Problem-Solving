import random
import os
import re

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("\n")
    print("Rock, Paper, Scissors - Shoot!")
    print(" Enter 'q' for quit")

    user_choice = input("Choose your weapon [r]ock, [p]aper, or [s]cissors: ")

    if user_choice == 'q':
        print("Quit...")
        break
    else:

        if not re.match("[RrPpSs]", user_choice):
            print("Please choose a letter [[R/r] or [P/p] or []S/s]")
            continue

        print("I choose: " + user_choice)
        opponenet_choice = random.choice(['r', 'p', 's'])
        print("Computer choose: " + opponenet_choice)

        if user_choice.lower() == opponenet_choice:
            print("Tie!")

        elif user_choice.lower() == 'r' and opponenet_choice == 's':
            print("I win!")
            continue

        elif user_choice.lower() == 'p' and opponenet_choice == 'r':
            print("I win! ")
            continue

        elif user_choice.lower() == 's' and opponenet_choice == 'p':
            print("I win!")
            continue

        else:
            print("Computer win!")
