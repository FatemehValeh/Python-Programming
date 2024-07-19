import random


def get_compute_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "* * *  = Tie! = * * *"
    elif (user_choice == "Rock" and computer_choice == "Paper") or \
            (user_choice == "Paper" and computer_choice == "Rock") or \
            (user_choice == "Rock" and computer_choice == "Scissors"):
        return "* * * **Win!** * * *"
    else:
        return "* * * Computer Won! You Lose * * *"


def main():
    print("Rock Paper Scissors")
    while True:
        print("1. New Game")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            user_choice = input("Enter your choice: [[R]ock, [P]aper, [S]cissors]: ")
            if user_choice not in ["R", "P", "S"]:
                print("Not a valid input. Please try again.")
                continue

            computer_choice = get_compute_choice()
            print(f"Computer choice: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)
            print(result)

        elif choice == "2":
            print("Exiting the game.")
            break

        else:
            print("Invalid input. Please try again.")


if __name__ == '__main__':
    main()
