# ------------ TIC TAC TOE ----------------

# ------------- Game set up ---------------
board = ["-","-","-","-","-","-","-","-","-"]

# Print board
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

player = "X"

# ------------- Start game --------------
# Place an X (or O) in one of the 9 slots
position = input("Please choose a position from 1-9: ")

# Type casting: changing from one type of object to another
# We do this because the input() function saves the value as a string (for example, "5" instead of 5)
position = int(position)

board[position - 1] = player

# Print board
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# Check if game won
# Row
row_1 = board[0] == board[1] == board[2] != "-"
row_2 = board[3] == board[4] == board[5] != "-"
row_3 = board[6] == board[7] == board[8] != "-"

# Column
column_1 = board[0] == board[3] == board[6] != "-"
column_2 = board[1] == board[4] == board[7] != "-"
column_3 = board[2] == board[5] == board[8] != "-"

# Diagonal
diagonal_1 = board[0] == board[4] == board[8] != "-"
diagonal_2 = board[2] == board[4] == board[6] != "-"

winner = row_1 + row_2 + row_3 + column_1 + column_2 + column_3 + diagonal_1 + diagonal_2

if winner >= 1:
    print("Player " + player + " won!")
    exit()
elif "-" not in board:
    print("It's a tie!")
    exit()

# Switch players
if player == "X":
    player = "O"
else:
    player = "X"

print("Player " + player + "'s turn.")

# ----------------- Loop ------------------
# Repeat the same code 8 more times since the game can have a maximum of 9 rounds

# ----------------- Round 2 -----------------
position = input("Please choose a position from 1-9: ")
position = int(position)

board[position - 1] = player

# Print board
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# Check if game won
row_1 = board[0] == board[1] == board[2] != "-"
row_2 = board[3] == board[4] == board[5] != "-"
row_3 = board[6] == board[7] == board[8] != "-"

column_1 = board[0] == board[3] == board[6] != "-"
column_2 = board[1] == board[4] == board[7] != "-"
column_3 = board[2] == board[5] == board[8] != "-"

diagonal_1 = board[0] == board[4] == board[8] != "-"
diagonal_2 = board[2] == board[4] == board[6] != "-"

winner = row_1 + row_2 + row_3 + column_1 + column_2 + column_3 + diagonal_1 + diagonal_2

if winner >= 1:
    print("Player " + player + " won!")
    exit()
elif "-" not in board:
    print("It's a tie!")
    exit()

# Switch players
if player == "X":
    player = "O"
else:
    player = "X"

print("Player " + player + "'s turn.")

# ----------------- Round 3 -----------------
position = input("Please choose a position from 1-9: ")
position = int(position)

board[position - 1] = player

# Print board
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# Check if game won
row_1 = board[0] == board[1] == board[2] != "-"
row_2 = board[3] == board[4] == board[5] != "-"
row_3 = board[6] == board[7] == board[8] != "-"

column_1 = board[0] == board[3] == board[6] != "-"
column_2 = board[1] == board[4] == board[7] != "-"
column_3 = board[2] == board[5] == board[8] != "-"

diagonal_1 = board[0] == board[4] == board[8] != "-"
diagonal_2 = board[2] == board[4] == board[6] != "-"

winner = row_1 + row_2 + row_3 + column_1 + column_2 + column_3 + diagonal_1 + diagonal_2

if winner >= 1:
    print("Player " + player + " won!")
    exit()
elif "-" not in board:
    print("It's a tie!")
    exit()

# Switch players
if player == "X":
    player = "O"
else:
    player = "X"

print("Player " + player + "'s turn.")

# ----------------- Round 4 -----------------
position = input("Please choose a position from 1-9: ")
position = int(position)

board[position - 1] = player

# Print board
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# Check if game won
row_1 = board[0] == board[1] == board[2] != "-"
row_2 = board[3] == board[4] == board[5] != "-"
row_3 = board[6] == board[7] == board[8] != "-"

column_1 = board[0] == board[3] == board[6] != "-"
column_2 = board[1] == board[4] == board[7] != "-"
column_3 = board[2] == board[5] == board[8] != "-"

diagonal_1 = board[0] == board[4] == board[8] != "-"
diagonal_2 = board[2] == board[4] == board[6] != "-"

winner = row_1 + row_2 + row_3 + column_1 + column_2 + column_3 + diagonal_1 + diagonal_2

if winner >= 1:
    print("Player " + player + " won!")
    exit()
elif "-" not in board:
    print("It's a tie!")
    exit()

# Switch players
if player == "X":
    player = "O"
else:
    player = "X"

print("Player " + player + "'s turn.")

# ----------------- Round 5 -----------------
position = input("Please choose a position from 1-9: ")
position = int(position)

board[position - 1] = player

# Print board
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# Check if game won
row_1 = board[0] == board[1] == board[2] != "-"
row_2 = board[3] == board[4] == board[5] != "-"
row_3 = board[6] == board[7] == board[8] != "-"

column_1 = board[0] == board[3] == board[6] != "-"
column_2 = board[1] == board[4] == board[7] != "-"
column_3 = board[2] == board[5] == board[8] != "-"

diagonal_1 = board[0] == board[4] == board[8] != "-"
diagonal_2 = board[2] == board[4] == board[6] != "-"

winner = row_1 + row_2 + row_3 + column_1 + column_2 + column_3 + diagonal_1 + diagonal_2

if winner >= 1:
    print("Player " + player + " won!")
    exit()
elif "-" not in board:
    print("It's a tie!")
    exit()

# Switch players
if player == "X":
    player = "O"
else:
    player = "X"

print("Player " + player + "'s turn.")

# ----------------- Round 6 -----------------
position = input("Please choose a position from 1-9: ")
position = int(position)

board[position - 1] = player

# Print board
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# Check if game won
row_1 = board[0] == board[1] == board[2] != "-"
row_2 = board[3] == board[4] == board[5] != "-"
row_3 = board[6] == board[7] == board[8] != "-"

column_1 = board[0] == board[3] == board[6] != "-"
column_2 = board[1] == board[4] == board[7] != "-"
column_3 = board[2] == board[5] == board[8] != "-"

diagonal_1 = board[0] == board[4] == board[8] != "-"
diagonal_2 = board[2] == board[4] == board[6] != "-"

winner = row_1 + row_2 + row_3 + column_1 + column_2 + column_3 + diagonal_1 + diagonal_2

if winner >= 1:
    print("Player " + player + " won!")
    exit()
elif "-" not in board:
    print("It's a tie!")
    exit()

# Switch players
if player == "X":
    player = "O"
else:
    player = "X"

print("Player " + player + "'s turn.")

# ----------------- Round 7 -----------------
position = input("Please choose a position from 1-9: ")
position = int(position)

board[position - 1] = player

# Print board
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# Check if game won
row_1 = board[0] == board[1] == board[2] != "-"
row_2 = board[3] == board[4] == board[5] != "-"
row_3 = board[6] == board[7] == board[8] != "-"

column_1 = board[0] == board[3] == board[6] != "-"
column_2 = board[1] == board[4] == board[7] != "-"
column_3 = board[2] == board[5] == board[8] != "-"

diagonal_1 = board[0] == board[4] == board[8] != "-"
diagonal_2 = board[2] == board[4] == board[6] != "-"

winner = row_1 + row_2 + row_3 + column_1 + column_2 + column_3 + diagonal_1 + diagonal_2

if winner >= 1:
    print("Player " + player + " won!")
    exit()
elif "-" not in board:
    print("It's a tie!")
    exit()

# Switch players
if player == "X":
    player = "O"
else:
    player = "X"

print("Player " + player + "'s turn.")

# ----------------- Round 8 -----------------
position = input("Please choose a position from 1-9: ")
position = int(position)

board[position - 1] = player

# Print board
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# Check if game won
row_1 = board[0] == board[1] == board[2] != "-"
row_2 = board[3] == board[4] == board[5] != "-"
row_3 = board[6] == board[7] == board[8] != "-"

column_1 = board[0] == board[3] == board[6] != "-"
column_2 = board[1] == board[4] == board[7] != "-"
column_3 = board[2] == board[5] == board[8] != "-"

diagonal_1 = board[0] == board[4] == board[8] != "-"
diagonal_2 = board[2] == board[4] == board[6] != "-"

winner = row_1 + row_2 + row_3 + column_1 + column_2 + column_3 + diagonal_1 + diagonal_2

if winner >= 1:
    print("Player " + player + " won!")
    exit()
elif "-" not in board:
    print("It's a tie!")
    exit()

# Switch players
if player == "X":
    player = "O"
else:
    player = "X"

print("Player " + player + "'s turn.")

# ----------------- Round 9 -----------------
position = input("Please choose a position from 1-9: ")
position = int(position)

board[position - 1] = player

# Print board
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

# Check if game won
row_1 = board[0] == board[1] == board[2] != "-"
row_2 = board[3] == board[4] == board[5] != "-"
row_3 = board[6] == board[7] == board[8] != "-"

column_1 = board[0] == board[3] == board[6] != "-"
column_2 = board[1] == board[4] == board[7] != "-"
column_3 = board[2] == board[5] == board[8] != "-"

diagonal_1 = board[0] == board[4] == board[8] != "-"
diagonal_2 = board[2] == board[4] == board[6] != "-"

winner = row_1 + row_2 + row_3 + column_1 + column_2 + column_3 + diagonal_1 + diagonal_2

if winner >= 1:
    print("Player " + player + " won!")
    exit()
elif "-" not in board:
    print("It's a tie!")
    exit()