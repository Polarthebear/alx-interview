#!/usr/bin/python3
"""N Queens Module"""

import sys


def find_n_queen_solutions(n):
    """Create valid solutions for N-Queens placement."""
    solutions = [[]]
    for row in range(n):
        solutions = add_queen(row, n, solutions)
    return solutions


def add_queen(row, n, partial_solutions):
    """Add queen to each valid solution for current row."""
    new_solutions = []
    for solution in partial_solutions:
        for col in range(n):
            if is_position_safe(row, col, solution):
                new_solutions.append(solution + [col])
    return new_solutions


def is_position_safe(new_row, new_col, solution):
    """func checks if queen can be placed with no conflict."""
    for existing_row, existing_col in enumerate(solution):
        if existing_col == new_col or abs(existing_col - new_col) == abs(existing_row - new_row):
            return False
    return True


def parse_input():
    """Parse and validate CLI input."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def solve_n_queens():
    """Solve N-Queens problem and print solution."""
    n = parse_input()
    solutions = find_n_queen_solutions(n)
    for solution in solutions:
        print([[row, col] for row, col in enumerate(solution)])


if __name__ == '__main__':
    solve_n_queens()
