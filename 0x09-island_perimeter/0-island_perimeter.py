#!/usr/bin/python3

"""
Module for island_perimeter function
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    Args:
        grid (list): A list of list of integers rep the island
    Returns:
        int: The perimeter of the island
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            perimeter += 4  # Each land cell contributes 4 to the perimeter

            # Check adjacent cells, and subtract 1 for each neighbouring land
            # cell
            if i > 0 and grid[i - 1][j] == 1:
                perimeter -= 1
            if i < len(grid) - 1 and grid[i + 1][j] == 1:
                perimeter -= 1
            if j > 0 and grid[i][j - 1] == 1:
                perimeter -= 1
            if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                perimeter -= 1

    return perimeter
