"""
Create a simple game of tic, tac, toe:

- Prompt the two players for their name
- At each turn write whose turn it is and whether they are "X" or "O", i.e. "Player 1 (X) turn:"
- Prompt the user for which cell they want to place their next symbol in (1-indexed), e.g. 1, 1 is the top left corner
- Show the board after each turn
- After each turn, you must check if someone has won
- End game if someone wins or it is a draw
- When a game ends you must print "The winner is <player_name> or "Draw" if it is a draw

An empty board is represented by:
```
             |     |
             |     |
        _____|_____|_____
             |     |
             |     |
        _____|_____|_____
             |     |
             |     |
             |     |
```
"""


player1 = input("Player x name: ")
player2 = input("Player o name: ")



def print_tic_tac_toe(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("\t     |     |")
    print("\n")

def has_won(board):
    # check rows
    for i in range(3):
        if board[i*3] != " " and board[i*3] == board[i*3 + 1] == board[i*3 + 2]:
            return True
        
    # check columns
    for i in range(3):
        if board[i] != " " and board[i] == board[i + 3] == board[i + 6]:
            return True
        
    # check diagonals
    if board[0] != " " and board[0] == board[4] == board[8]:
        return True
    if board[2] != " " and board[2] == board[4] == board[6]:
        return True
    
    return False

# init board
board = [" "]*9
print_tic_tac_toe(board)

for i in range(9):
    symbol = "X" if i % 2 == 0 else "O"
    
    if symbol == "X":
        turn = input(f"{player1} (X) turn: ")
    else:
        turn = input(f"{player2} (O) turn: ")
        
    row, col = turn.split(",")
    row = int(row.strip()) - 1
    col = int(col.strip()) - 1
    
    board[row*3 + col] = symbol
    
    print_tic_tac_toe(board)
    
    # check if someone has won
    if has_won(board):
        if symbol == "X":
            print(f"The winner is {player1}")
        else:
            print(f"The winner is {player2}")
        break
    
    if i == 8:
        print("Draw")
        break
    