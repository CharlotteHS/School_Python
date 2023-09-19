#python challenge 7
import random
#enables random variables

rps = ["rock", "paper", "scissors"]
#list with all the options

computer_move = random.choice(rps)
#setting the variable to choose randomly from the list

player_move = input("Enter your move here::: ")

if player_move == "rock":
    print(computer_move)

    if computer_move == "rock":
        print("It's a draw")

    if computer_move == "paper":
        print("Computer wins")

    if computer_move == "scissors":
        print("You win")

if player_move == "paper":
    print(computer_move)

    if computer_move == "rock":
        print("You win")

    if computer_move == "paper":
        print("Its a draw")

    if computer_move == "scissors":
        print("Computer wins")

if player_move == "scissors":
    print(computer_move)

    if computer_move == "rock":
        print("Computer wins")

    if computer_move == "paper":
        print("You win")

    if computer_move == "scissors":
        print("It's a draw")