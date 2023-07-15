# ------ Global variables ------
# Game board
board = ["-" for _ in range(36)]

# If the game is still going
game_still_going = True

# Who won? tie?
winner = None

# Whose turn is it?
current_player = "X"


# Display board
def display_board():
    # Board outline
    for i in range(0, 36, 6):
        # Create rows
        row = board[i:i + 6]
        print(" | ".join(row))


# Play a game of tic-tac-toe
def play_game():
    # Display initial board
    display_board()

    # While the game is still going
    while game_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif not winner:
        print("Tie")


# Handle a single turn of an arbitrary player
def handle_turn(player):
    # Create validation to check for number, and valid play spot
    valid_position = False
    while not valid_position:
        position = input("Choose a position from 1-36: ")
        if position.isdigit():
            position = int(position) - 1
            if 0 <= position < 36 and board[position] == "-":
                valid_position = True

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # Set up global variables
    global game_still_going, winner

    # Check rows
    row_winner = check_rows()

    # Check columns
    column_winner = check_columns()

    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner or column_winner or diagonal_winner:
        game_still_going = False
        winner = row_winner or column_winner or diagonal_winner

    return


def check_rows():
    # Same logic as the board logic
    for i in range(0, 36, 6):
        row = board[i:i + 6]
        # Amazing, use all() to see if all elements in the sublist match row[0]
        if all(cell == row[0] and cell != "-" for cell in row):
            return row[0]
    return None


def check_columns():
    # same as above, but with columns
    for i in range(6):
        column = [board[j] for j in range(i, 36, 6)]
        if all(cell == column[0] and cell != "-" for cell in column):
            return column[0]
    return None


def check_diagonals():
    diagonals = [
        [board[0], board[7], board[14], board[21], board[28], board[35]],
        [board[5], board[10], board[15], board[20], board[25], board[30]]
    ]
    for diagonal in diagonals:
        if all(cell == diagonal[0] and cell != "-" for cell in diagonal):
            return diagonal[0]
    return None


def check_if_tie():
    # Global variable
    global game_still_going
    # Check if all squares have been played
    if "-" not in board:
        game_still_going = False


def flip_player():
    # Global variable
    global current_player
    # If the current player is X, change it to O. Else, change it to X
    current_player = "O" if current_player == "X" else "X"


play_game()


