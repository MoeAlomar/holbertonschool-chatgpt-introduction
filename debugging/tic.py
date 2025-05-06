#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # Input with validation
        try:
            row = int(input(f"Enter row (0-2) for player {current_player}: "))
            col = int(input(f"Enter column (0-2) for player {current_player}: "))
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid move. Row and column must be 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
