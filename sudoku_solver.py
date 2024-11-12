import numpy as np

# Function to check if a number can be placed at a given position
def is_safe(board, row, col, num):
    # Check if the number exists in the row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    # Check the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

# Backtracking algorithm to solve the Sudoku
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty spot
                for num in range(1, 10):  # Try numbers 1-9
                    if is_safe(board, row, col, num):
                        board[row][col] = num  # Place the number
                        if solve(board):  # Recursively solve
                            return True
                        board[row][col] = 0  # Backtrack if no solution found
                return False  # If no number works, return False
    return True  # Puzzle solved

# Initial Sudoku puzzle (0 represents empty spaces)
initial_board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a plot for visualizing the Sudoku grid
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xticks(np.arange(0, 9, 1))
ax.set_yticks(np.arange(0, 9, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)

# Function to draw the grid and display numbers
def draw_grid(board):
    ax.clear()
    ax.set_xticks(np.arange(0, 9, 1))
    ax.set_yticks(np.arange(0, 9, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    
    # Draw the Sudoku grid
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                ax.text(col + 0.5, 8 - row + 0.5, str(board[row][col]), ha='center', va='center', fontsize=20)
                
    # Draw thick lines for 3x3 subgrids
    for x in range(1, 9):
        linewidth = 2 if x % 3 == 0 else 0.5
        ax.axhline(x - 0.5, color='black', lw=linewidth)
        ax.axvline(x - 0.5, color='black', lw=linewidth)

# Animation function to update the grid at each step
def update(frame):
    if frame < len(solve_steps):
        draw_grid(solve_steps[frame])
    return []

# Solving the Sudoku and storing each step
solve_steps = []
def solve_with_animation(board):
    if solve(board):
        return True
    return False

# Modify the solver to track each step
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty spot
                for num in range(1, 10):  # Try numbers 1-9
                    if is_safe(board, row, col, num):
                        board[row][col] = num  # Place the number
                        solve_steps.append(board.copy())  # Store the board state after the move
                        if solve(board):  # Recursively solve
                            return True
                        board[row][col] = 0  # Backtrack if no solution found
                        solve_steps.append(board.copy())  # Store the board after backtracking
                return False  # If no number works, return False
    return True  # Puzzle solved

# Start the animation after solving the Sudoku
solve_with_animation(initial_board)

# Create animation
ani = FuncAnimation(fig, update, frames=len(solve_steps), interval=500, repeat=False)

# Display the animation
plt.show()
