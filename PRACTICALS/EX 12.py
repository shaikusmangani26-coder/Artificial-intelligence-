
# Tic Tac Toe Game in Python

board = [" " for _ in range(9)]


def display_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def play_game():
    player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Enter a position from 1 to 9.")
    print("Positions are arranged as follows:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    while True:
        display_board()

        try:
            position = int(input(
                f"Player {player}, enter position (1-9): "
            ))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if position < 1 or position > 9:
            print("Choose a position between 1 and 9.")
            continue

        if board[position - 1] != " ":
            print("Position already occupied! Try again.")
            continue

        board[position - 1] = player

        if check_winner(player):
            display_board()
            print(f"Player {player} wins!")
            break

        if " " not in board:
            display_board()
            print("The game is a draw!")
            break

        player = "O" if player == "X" else "X"


play_game()
