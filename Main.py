import random


def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()

    while player_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player_choice = input("Enter a choice (rock, paper, scissors): ").lower()

    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}.")

    if player == computer:
        return "tie"

    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if win_conditions[player] == computer:
        return "player"
    else:
        return "computer"


player_wins = 0
computer_wins = 0

while True:
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])

    if result == "player":
        player_wins += 1
        print(f"{choices['player'].capitalize()} beats {choices['computer']}. You win!")
    elif result == "computer":
        computer_wins += 1
        print(f"{choices['computer'].capitalize()} beats {choices['player']}. You lose!")
    else:
        print("It's a tie!")

    print(f"You have won {player_wins} times and the computer has won {computer_wins} times.")

    while True:
        retry = input("Do you want to try again? Y/N: ").upper()
        if retry == "N":
            print("Have a nice day!")
            exit()
        elif retry == "Y":
            break
        else:
            print("Invalid input, please enter Y or N.")
