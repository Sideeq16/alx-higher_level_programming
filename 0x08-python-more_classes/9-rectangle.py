#!/usr/bin/python3

import sys
"""Documentation of a square class"""


def is_safe(board, row, col, n):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check the upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check the lower left diagonal
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def solve(board, col, n, solutions):
    # Base case: all columns are filled
    if col == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True
    # Recursive case: try placing a queen in each row of the current column
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1 # Place a queen
            res = solve(board, col + 1, n, solutions) or res # Recur for next column
            board[i][col] = 0 # Backtrack and remove the queen
    return res

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    # Check if N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    # Initialize an empty board
    board = [[0 for i in range(n)] for j in range(n)]
    # Initialize an empty list of solutions
    solutions = []
    # Solve the problem and print the solutions
    solve(board, 0, n, solutions)
    print_solutions(solutions)
