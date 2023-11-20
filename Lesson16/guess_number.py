import sys
from random import choice


def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        playerchoice = input(
            f'\n{name}, guess the number I am thinking of 1, 2 or 3. \n\n')

        if playerchoice not in ["1", "2", "3"]:
            print(f'{name}, please must enter 1, 2 or 3.')
            return play_guess_number()

        player = int(playerchoice)

        computerChoice = choice("123")

        computer = int(computerChoice)

        print(f'{name} chose {str(playerchoice)}')

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            print(f'I was thinking of about the number {computerChoice}.')

            if player == computer:
                player_wins += 1
                return f'\n\n🎉 {name} you win!'
            else:
                python_wins += 1
                return f"\n\nSorry, {name}. Better luck next time. 😔"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")

        print(f"\nWinning percentage: {round(player_wins/game_count * 100)}%")

        print("\nPlay again, {name}?")

        while True:
            playAgain = input("\nY for yes or \nQ to quit \n")
            if playAgain.lower() not in ['y', 'q']:
                continue
            else:
                break
        if playAgain.lower() == "y":
            return play_guess_number()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            return
        
    return play_guess_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personilized game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()
    guess_num = guess_number(args.name)

guess_my_number = guess_number()

if __name__ == '__main__':
    guess_my_number()
