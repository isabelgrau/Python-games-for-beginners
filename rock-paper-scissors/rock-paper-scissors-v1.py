import random
moves = ["rock","paper","scissors"]
random1 = random.randint(1,3)
random2 = random.randint(1,3)

player1 = moves[random1 - 1]
player2 = moves[random2 - 1]

print("Player 1: " + player1)
print("Player 2: " + player2)

if player1 == "rock":
    if player2 == "rock":
        print("It's a tie!")
    elif player2 == "paper":
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins!")
    elif player2 == "paper":
        print("It's a tie!")
    else:
        print("Player 2 wins!")
else:
    if player2 == "rock":
        print("Player 2 wins!")
    elif player2 == "paper":
        print("Player 1 wins!")
    else:
        print("It's a tie!")
