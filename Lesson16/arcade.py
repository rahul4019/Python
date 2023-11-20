import sys
from guess_number import guess_my_number
from rps import rock_paper_scissiors


def arcade(name="PlayerOne"):
    print(f"{name}, welcome to the Arcade! 🤖")

    print(f'Please choose a game:')

    option = input(
        '\n1 = Rock Paper Scissiors\n2 = Guess My Number\n\nOr press "X" to exit the Arcade\n')

    if option.lower() == 'x':
        sys.exit(f"Bye {name}! 👋")

    if option not in ["1", "2"]:
        print("You must enter 1 or 2.")
        return arcade()

    user_option = int(option)

    if user_option == 1:
        print("option 1 selected")
        rock_paper_scissiors()
        arcade()
    else:
        guess_my_number()
        arcade()


arcade("Rahul")
