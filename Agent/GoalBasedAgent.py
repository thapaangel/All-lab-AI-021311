import matplotlib.pyplot as plt
import numpy as np
import random
import time

WIDTH, HEIGHT = 6, 6
DIRT_PROBABILITY = 0.3
DELAY = 0.3  # seconds

# Directions: king-like moves (8 directions)
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

room = [[1 if random.random() < DIRT_PROBABILITY else 0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
agent = [random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1)]
steps = 0

def all_clean():
    return all(cell == 0 for row in room for cell in row)

def draw_room():
    grid = np.ones((HEIGHT, WIDTH, 3)) * 0.8  # light gray background
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if room[i][j] == 1:
                grid[i, j] = [0.6, 0.3, 0]  # brown dirt
    grid[agent[0], agent[1]] = [1, 1, 1]  # white agent cell
    plt.imshow(grid)
    plt.title(f"Step: {steps}")
    plt.axis('off')

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def next_move_towards(target):
    # Move agent one step toward the target using king-like moves minimizing Manhattan distance
    best_move = agent
    best_dist = manhattan_distance(agent, target)
    for dx, dy in directions:
        nx, ny = agent[0] + dx, agent[1] + dy
        if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
            dist = manhattan_distance((nx, ny), target)
            if dist < best_dist:
                best_dist = dist
                best_move = [nx, ny]
    return best_move

plt.ion()  # interactive mode on

while not all_clean():
    # If current cell is dirty, clean it
    if room[agent[0]][agent[1]] == 1:
        room[agent[0]][agent[1]] = 0
    else:
        # Find all dirty cells
        dirty_cells = [(i, j) for i in range(HEIGHT) for j in range(WIDTH) if room[i][j] == 1]
        if dirty_cells:
            # Find closest dirty cell
            target = min(dirty_cells, key=lambda c: manhattan_distance(agent, c))
            # Move one step toward the target
            agent = next_move_towards(target)
        else:
            # No dirt found, just stay
            pass

    steps += 1
    draw_room()
    plt.draw()
    plt.pause(DELAY)
    plt.clf()

plt.ioff()
print("Cleaning complete!")
print(f"Total steps: {steps}")
