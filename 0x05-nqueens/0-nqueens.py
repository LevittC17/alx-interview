#!/usr/bin/python3


import sys


def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_n_queens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solutions = []

    def solve(row):
        if row == n:
            solutions.append(board[:])
        for i in range(n):
            if is_safe(board, i, row):
                board[row] = i
                solve(row + 1)

    solve(0)

    for solution in solutions:
        print([[i, j] for i, j in enumerate(solution)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        solve_n_queens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
