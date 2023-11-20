import sys
import random
from enum import Enum


def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f'\n{name},please enter... \n 1 for Rock, \n 2 for Paper, or \n 3 for Scissors:\n\n')

        if playerchoice not in ["1", "2", "3"]:
            print(f'{name}, please must enter 1, 2 or 3.')
            return play_rps()

        player = int(playerchoice)

        computerChoice = random.choice("123")

        computer = int(computerChoice)

        print(f"{name} chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name} win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name} win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name} win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}...😔"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print("\nPlay again, {name}?")

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
            return

    return play_rps


rock_paper_scissiors = rps()

if __name__ == '__main__':
    rock_paper_scissiors()
