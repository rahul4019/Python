import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input(
        'Enter... \n 1 for Rock, \n 2 for Paper, or \n 3 for Scissors:\n\n')

    if playerchoice not in ["1", "2", "3"]:
        print('You must enter 1, 2 or 3.')
        return play_rps()

    player = int(playerchoice)

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    print("")
    print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    print("")

    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print('😲 Tie game!')
    else:
        print("🐍 Python wins!")

    print("\nPlay again?")

    while True:
        playAgain = input("\nY for Yes or \nQ to Quit \n")
        if playAgain.lower() not in ['y', 'q']:
            continue
        else:
            break

    if playAgain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")


play_rps()
