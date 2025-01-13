# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:23:11 2025

@author: thoom
"""

import random
import os
import time

# Constantes
LIVE_CELL = '#'
DEAD_CELL = ' '

def create_grid(rows, cols):
    """Crée une grille aléatoire pour le jeu avec des cellules vivantes et mortes."""
    return [[LIVE_CELL if random.random() > 0.8 else DEAD_CELL for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    """Affiche la grille dans la console."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Nettoyer la console
    for row in grid:
        print(''.join(row))
    time.sleep(0.5)  # Pause pour permettre de voir l'évolution

def count_neighbors(grid, row, col):
    """Compte le nombre de voisins vivants autour d'une cellule."""
    rows, cols = len(grid), len(grid[0])
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue  # Ignorer la cellule actuelle
            if 0 <= row + i < rows and 0 <= col + j < cols:
                if grid[row + i][col + j] == LIVE_CELL:
                    neighbors += 1
    return neighbors

def next_generation(grid):
    """Calcule la prochaine génération de la grille."""
    rows, cols = len(grid), len(grid[0])
    new_grid = [[DEAD_CELL for _ in range(cols)] for _ in range(rows)]
    
    for row in range(rows):
        for col in range(cols):
            neighbors = count_neighbors(grid, row, col)
            if grid[row][col] == LIVE_CELL:
                if neighbors in [2, 3]:
                    new_grid[row][col] = LIVE_CELL
                else:
                    new_grid[row][col] = DEAD_CELL
            else:
                if neighbors == 3:
                    new_grid[row][col] = LIVE_CELL
    
    return new_grid

def play_game_of_life(rows, cols, generations):
    """Lance le jeu de la vie avec une grille de dimensions données et un certain nombre de générations."""
    grid = create_grid(rows, cols)
    for _ in range(generations):
        print_grid(grid)
        grid = next_generation(grid)

if __name__ == "__main__":
    play_game_of_life(20, 40, 100)  # Grille 20x40 avec 100 générations
