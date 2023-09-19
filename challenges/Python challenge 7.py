#python challenge 7
import random

rps = ["rock", "paper", "scissors"]

computer_move = random.choice(rps)

player_move = input("Enter your move here::: ")

if player_move == "rock":
    print(computer_move)

    if computer_move == "rock":
        print("It's a draw")

    if computer_move == "paper":
        print("Computer wins")

    if computer_move == "scissors":
        print("You win")
        