# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:42:17 2025

@author: cypri
"""

import time
import os

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join(row))
    print()

def next_generation(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[' ' for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            live_neighbors = sum(
                grid[r+dr][c+dc] == '#' 
                for dr in [-1, 0, 1] 
                for dc in [-1, 0, 1]
                if (dr != 0 or dc != 0) and 0 <= r+dr < rows and 0 <= c+dc < cols
            )
            if grid[r][c] == '#' and live_neighbors in [2, 3]:
                new_grid[r][c] = '#'
            elif grid[r][c] == ' ' and live_neighbors == 3:
                new_grid[r][c] = '#'
    return new_grid

if __name__ == "__main__":
    grid = [
        [' ', '#', ' '],
        [' ', '#', ' '],
        ['#', '#', '#']
    ]
    while True:
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(1)
