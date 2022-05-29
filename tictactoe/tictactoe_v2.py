# ------- TIC TAC TOE [FULL VERSION] -------

# ------------- Game set up ---------------
board = ["-","-","-","-","-","-","-","-","-"]

def display_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

player = "X"
game_ongoing = True

# ------------- Start game --------------
print("Let's play!")
display_board()

while game_ongoing == True:
    while True:
        try:
            position = int(input("Please choose a position from 1-9: "))

            if position < 1 or position > 9:
                print("That is not a valid position.\n")
                continue
            elif board[position - 1] != "-":
                print("That position is taken. Please choose another position.\n")
                continue

        except ValueError:
            print("That is not a valid position.\n")
            continue
        else:
            break

    board[position - 1] = player
    display_board()

    # Check if game won
    # rows
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # columns
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    # diagonals
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    winner = row_1 + row_2 + row_3 + col_1 + col_2 + col_3 + diagonal_1 + diagonal_2

    if winner >= 1:
        print("\nPlayer " + player + " won!")
        game_ongoing = False
        continue
    elif "-" not in board:
        print("\nIt's a tie!")
        game_ongoing = False
        continue

    if player == "X":
        player = "O"
    else:
        player = "X"

    print("\nPlayer " + player + "'s turn.")