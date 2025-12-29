# Greedy and Backtracking Maze Solver

## Description

This Python project implements greedy and backtracking algorithms to solve mazes. It finds all possible paths from the start ('S') to the goal ('G'), identifies the shortest (optimal) path, and visualizes the maze-solving process using the Turtle graphics library. The maze is represented as a 2D grid with walls ('#') and open paths (' '), and the solver animates the turtle's movement through the maze for both algorithms.

The greedy approach uses a depth-first search (DFS) with a stack to explore paths, while the backtracking method recursively explores all possibilities, backtracking when necessary. Both methods output the paths found and highlight the shortest one.

## Features

- **Maze Representation**: A predefined 2D list representing the maze with walls, start, and end points.
- **Greedy Solver**: Explores paths using a stack-based approach, simulating a greedy search.
- **Backtracking Solver**: Recursively finds all valid paths and identifies the shortest one.
- **Visualization**: Uses Python's Turtle module to draw the maze and animate the solver's path, including rotations and movements.
- **Output**: Prints all paths, the shortest path, and solves the maze in both greedy and backtracking modes.
- **Customizable**: The maze layout can be easily modified in the code.

## Requirements

- Python 3.x
- Turtle (included in Python's standard library)

No additional libraries are required.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/greedy-backtracking-maze-solver.git
   cd greedy-backtracking-maze-solver
   ```

No further installation is needed as it uses standard Python libraries.

## Usage

1. Run the script:
   ```
   python Greedy-and-Backtracking-Maze-Solver.py
   ```

2. The program will:
   - Draw the maze using Turtle.
   - Solve the maze first using the greedy approach, printing paths and the shortest path.
   - Then solve it using backtracking, printing all solutions and the shortest path.
   - Animate the turtle moving through the maze for both methods.

The maze is hardcoded in the script, but you can modify the `maze` list to create custom mazes.

Example output in the console:
```
Solving maze in a Greedy way

Path taken
[(1, 1), (2, 1), ...]  # List of coordinates visited

Shortest path
[(1, 1), (2, 1), ...]  # Coordinates of the optimal path

Solving maze in a Backtracking way

All solutions
[[(1, 1), ...], ...]  # List of all possible paths

Shortest path
[(1, 1), ...]  # Optimal path
```

A Turtle window will open showing the maze and the animated solving process.

## Code Structure

- `Greedy-and-Backtracking-Maze-Solver.py`: The main script containing:
  - Maze definition.
  - Turtle setup and drawing functions.
  - Greedy solver: `solve_maze_greedy`.
  - Backtracking solver: `solve_maze_backtracking`.
  - Helper functions for movement and rotation.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. Please ensure any changes include comments and maintain the code's readability.
