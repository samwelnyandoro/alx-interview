#!/usr/bin/python3
"""Island perimeter module"""


def island_perimeter(grid):
    """
    A function that determines the perimeter of an island based
    on the cells. land is 1 and water is 0. Each cell is 4units
    i.e perimeter of land surrounded by water = 4,
    perimeter of land with a neighbouring land is (perimeter - 2) each
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if (i > 0 and grid[i - 1][j] == 1):
                    perimeter -= 2
                if (j > 0 and grid[i][j - 1] == 1):
                    perimeter -= 2
    return perimeter
