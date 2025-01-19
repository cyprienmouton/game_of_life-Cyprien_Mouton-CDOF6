# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:42:17 2025

@author: cypri
"""

import time
import os

# Displays the grid along with the current generation number.
def print_grid(grid, generation):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Generation: {generation}")
    for row in grid:
        print(''.join(row))
    print()

# Computes the next generation of the grid based on Conway's Game of Life rules.
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
    generation = 0  # Compteur de générations
    while True:
        print_grid(grid, generation)
        grid = next_generation(grid)
        generation += 1
        time.sleep(1)
