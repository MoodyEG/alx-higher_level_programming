#!/usr/bin/python3
""" Queen Module """


def solvequeen(size):
    """ Solve the N-Queens problem using backtracking """
    board = [-1] * size
    backqueen(board, 0)


def backqueen(board, row):
    """ Recursive helper function to place queens on the board """
    if row == len(board):
        print_solution(board)
        return
    board[row] = -1
    while (board[row] < len(board) - 1):
        board[row] += 1
        if isvalid(board, row):
            backqueen(board, row + 1)


def isvalid(board, row):
    """ Check if placing a queen at this position is valid """
    for i in range(row):
        if board[i] == board[row]:
            return False
        if abs(board[i] - board[row]) == abs(i - row):
            return False
    return True


def print_solution(board):
    """ Print a solution of the N-Queens problem """
    sol = []
    for i in range(len(board)):
        sol.append([i, board[i]])
    print(sol)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        isinstance(int(sys.argv[1]), int)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    size = int(sys.argv[1])
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solvequeen(size)
