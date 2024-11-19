#!/usr/bin/python3
"""
2D Matrix Rotatin (Interview Prep)
"""


def rotate_2d_matrix(matrix):
    """Rotates a square 2D matrix 90 degrees clockwise in place."""
    if not matrix or not all(isinstance(row, list) for row in matrix):
        return
    if len(matrix) != len(matrix[0]):  # Ensure it's a square matrix
        raise ValueError("Only square matrices can be rotated in place.")

    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
