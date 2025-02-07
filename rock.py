import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

while True:
    print("\nRock, Paper, Scissors Game 🎮")
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    print(determine_winner(player_choice, computer_choice))

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 🎮 Goodbye!")
        break
