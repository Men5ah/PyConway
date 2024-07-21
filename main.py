#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

N = 100 # taille de la grille (size)
ON = 255
OFF = 0

def add_color(grid):
    '''
    Ajoute de la couleur aux cellules (add color)
    Cool colors : https://pigment.shapefactory.co/?d=0&s=0&a=DE2D43&b=E5E3E8
    '''
    color_grid = np.zeros((grid.shape[0], grid.shape[1], 3), dtype=np.uint8)
    color_grid[grid == ON] = np.array([222, 45, 67])
    color_grid[grid == OFF] = np.array([253, 253, 254])
    return color_grid

def update(grid, N):
    '''
    Fonction update (update function)
    '''
    nouvGrid = grid.copy()
    for a in range(N):
        for b in range(N):
            total = int((grid[a,(b-1)%N]+grid[a,(b+1)%N]+grid[(a-1)%N,b]+grid[(a+1)%N,b]+grid[(a-1)%N,(b-1)%N]+grid[(a-1)%N,(b+1)%N]+grid[(a+1)%N,(b-1)%N]+grid[(a+1)%N,(b+1)%N])/255)
            if grid[a, b]  == ON:
                #Rules 1 and 2
                # If a cell has less than 2 neighbours it dies
                # If a cell has more than 3 neighbors it dies
                if (total < 2) or (total > 5):
                    nouvGrid[a,b] = OFF            
            else:
                # Rule 4
                # If a dead cell has exactly 3 live neighbours it will come to life
                if total == 3:
                    nouvGrid[a,b] = ON
    return nouvGrid

def set_initial_condition(grid, coordinates):
    '''
    Set the initial condition based on user input coordinates
    coordinates is a list of tuples (x, y)
    '''
    for x, y in coordinates:
        grid[x % N, y % N] = ON

def main():
    '''
    Fonction principale (main function)
    '''
    # Initialize the grid with all cells set to OFF
    grid = np.full((N, N), OFF)
    
    # User-defined starting coordinates
        # Combined set of starting coordinates for multiple patterns
    starting_coords = [
        # Block (Still Life)
        (20, 20), (20, 21), (21, 20), (21, 21),
        # Blinker (Oscillator)
        (30, 31), (30, 32), (30, 33),
        # Glider (Spaceship)
        (40, 41), (41, 42), (42, 40), (42, 41), (42, 42),
        # Toad (Oscillator)
        (50, 51), (50, 52), (50, 53), (51, 50), (51, 51), (51, 52),
        # Beacon (Oscillator)
        (60, 60), (60, 61), (61, 60), (61, 61), (62, 62), (62, 63), (63, 62), (63, 63)
    ]
    set_initial_condition(grid, starting_coords)
    
    fig, ax = plt.subplots()
    img = ax.imshow(add_color(grid), interpolation='nearest')

    steps = 200  # Number of steps to run
    for _ in range(steps):
        grid = update(grid, N)
        img.set_data(add_color(grid))
        plt.pause(0.1)  # Pause to create the animation effect
    
    plt.show()

if __name__ == "__main__":
    main()