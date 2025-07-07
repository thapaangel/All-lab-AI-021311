import tkinter as tk
import random

# Parameters
WIDTH = 6
HEIGHT = 6
CELL_SIZE = 60
DIRT_PROBABILITY = 0.3
DELAY_MS = 300

# Directions (king-like movement)
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

# Initialize room with dirt
room = [[1 if random.random() < DIRT_PROBABILITY else 0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
visited_count = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Agent starting position
agent_pos = [random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1)]
path = [tuple(agent_pos)]
steps = 0

# Tkinter setup
root = tk.Tk()
root.title("Vacuum Cleaner Agent (Utility-Based)")
canvas = tk.Canvas(root, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE)
canvas.pack()

# Draw single cell
def draw_cell(i, j):
    x1 = j * CELL_SIZE
    y1 = i * CELL_SIZE
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE

    if [i, j] == agent_pos:
        canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='gray')
        canvas.create_text((x1+x2)//2, (y1+y2)//2, text="🤖", font=("Arial", 24))
    elif room[i][j] == 1:
        canvas.create_rectangle(x1, y1, x2, y2, fill='brown', outline='gray')
        canvas.create_text((x1+x2)//2, (y1+y2)//2, text="D", font=("Arial", 16), fill="white")
    else:
        canvas.create_rectangle(x1, y1, x2, y2, fill='lightgray', outline='gray')

# Redraw full room
def draw_room():
    canvas.delete("all")
    for i in range(HEIGHT):
        for j in range(WIDTH):
            draw_cell(i, j)

# Goal check
def goal_reached():
    return all(cell == 0 for row in room for cell in row)

# Utility calculation
def calculate_utility(x, y):
    utility = 0
    if room[x][y] == 1:
        utility += 100
    utility -= visited_count[x][y] * 5
    return utility

# Step function
def step():
    global steps
    x, y = agent_pos

    if room[x][y] == 1:
        room[x][y] = 0

    visited_count[x][y] += 1
    draw_room()
    steps += 1
    path.append((x, y))

    if goal_reached():
        print("\n🚀 Cleaning complete!")
        print(f"🔢 Total steps taken: {steps}")
        print("🔹 Agent path:")
        print(' -> '.join([f"({x},{y})" for x, y in path]))
        return

    best_utility = float('-inf')
    best_move = (x, y)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
            utility = calculate_utility(nx, ny)
            if utility > best_utility:
                best_utility = utility
                best_move = (nx, ny)

    agent_pos[0], agent_pos[1] = best_move
    root.after(DELAY_MS, step)

# Start simulation
draw_room()
root.after(DELAY_MS, step)
root.mainloop()
