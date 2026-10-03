# 8 Queens Problem using Backtracking

N = 8

def is_safe(board, row, col):
    # Check the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_queens(board, row):
    # All queens are placed
    if row == N:
        print_board(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col

            if solve_queens(board, row + 1):
                return True

            # Backtrack
            board[row] = -1

    return False


def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Start the program
board = [-1] * N

if not solve_queens(board, 0):
    print("No solution exists")
