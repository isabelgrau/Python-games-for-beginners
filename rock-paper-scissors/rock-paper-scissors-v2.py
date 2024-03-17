import random

actions = ["rock", "paper","scissors"]

player1 = input("Enter your choice (rock, paper, scissors): ")
player2 = random.choice(actions)

print("Player 1 chose " + player1 + " and player 2 chose " + player2)

# rock > scissors > paper > rock
if player1 == player2:
    print("It's a tie! Both players chose " + player1)

# if P1 plays rock
elif player1 == "rock":
    # if P2 plays paper
    if player2 == "paper":
        print("Paper covers rock! Player 2 wins!")

    # if P2 plays scissors
    else:
        print("Rock smashes scissors! Player 1 wins!")

# if P1 plays paper
elif player1 == "paper":
    # if P2 plays rock
    if player2 == "rock":
        print("Paper covers rock! Player 1 wins!")

    # if P2 plays scissors
    else:
        print("Scissors cuts paper! Player 2 wins!")

# if P1 plays scissors
elif player1 == "scissors":
    # if P2 plays rock
    if player2 == "rock":
        print("Rock smashes scissors! Player 2 wins!")

    #if P2 plays paper
    else:
        print("Scissors cuts paper! Player 1 wins!")
