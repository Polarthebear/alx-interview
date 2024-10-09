#!/usr/bin/python3
"""
Module for 0-pascal_triangle
Function returning list of lists
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers 
    representing the Pascal's tringle of n:
      Args ->
          n: input parameter of the function

      Returns:
          List of lists of integers(Success)
          Empty list (Fail)
    """
    triangle = []

    if n <= 0:
        return triangle
    
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)

    # Print triangle
    return triangle
