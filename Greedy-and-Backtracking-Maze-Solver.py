import turtle

"""
The following lines of code are to configure the Turtle window
"""
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze Solver with Turtle")
wn.setup(width=800, height=800)
pixels = 300

"""
The following "maze" list creates the maze represented by characters.

'#' represents the walls and ' ' (space) represents the free path
The 'S' represents the starting point and the 'G' represents the end of the route.
"""

maze = [
    "############",
    "#S         #",
    "########## #",
    "#          #",
    "# ##########",
    "# #        #",
    "# ######## #",
    "#          #",
    "# ##########",
    "#          #",
    "# ###### # #",
    "#        # #",
    "# ######## #",
    "#G#        #",
    "############"
]

"""
The following creates the class that allows drawing the maze"""
class MazeTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
    
    def change_color(self, coordinate_type):
        if coordinate_type == "start_point":
            self.color("green")
        elif coordinate_type == "end_point":
            self.color("yellow")
        elif coordinate_type == "default":
            self.color("black")
        

"""
The following creates the class that allows the turtle to be used as an object
"""
class SolverTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.speed(1)


"""
The following method draws the maze
"""
def draw_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == '#':
                maze_turtle.goto(x * 20 - pixels, pixels - y * 20)
                maze_turtle.stamp()
            elif maze[y][x] == 'S':
                start_pos = (x, y)
                maze_turtle.change_color("start_point")
                maze_turtle.goto(x * 20 - pixels, pixels - y * 20)
                maze_turtle.stamp()
                maze_turtle.change_color("default")
            elif maze[y][x] == 'G':
                end_pos = (x, y)
                maze_turtle.change_color("end_point")
                maze_turtle.goto(x * 20 - pixels, pixels - y * 20)
                maze_turtle.stamp()
                maze_turtle.change_color("default")
    return start_pos, end_pos


"""
The following method serves as an instruction to move the turtle to the 
next desired square of the maze
"""
def move_turtle(x, y):
    solver_turtle.goto(x * 20 - pixels, pixels - y * 20)


"""
The following method is the one that corresponds to work by the students.
It is the method responsible for solving the labyrinth.

It has 3 input arguments: The maze map, the starting position and
the target position.
"""




def solve_maze_greedy(maze, start, end):
    paths = []
    all_paths = set()
    best_path = []
    shortest_path_length = float('inf')
    move_order = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    stack = [(start, [])]
    visited = set()
    solver_turtle.speed(0)

    while stack:
        (x, y), path = stack.pop()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]
        all_paths.add((x, y))

        if (x, y) != start:
            solver_turtle.down()

        # Move and rotate
        if path:
            prev_x, prev_y = path[-2] if len(path) > 1 else (x, y)
            dx, dy = x - prev_x, y - prev_y
            move_turtle_and_rotate(x, y, (dx, dy))
        else:
            move_turtle(x, y)

        if (x, y) == end:
            if len(path) < shortest_path_length:
                best_path = path[:]
                shortest_path_length = len(path)
            continue

        for distance_x, distance_y in move_order:
            new_x, new_y = x + distance_x, y + distance_y
            if maze[new_y][new_x] != "#" and (new_x, new_y) not in visited:
                stack.append(((new_x, new_y), path))

    # Explore all remaining paths
    extra_stack = [start]
    extra_visited = set()
    while extra_stack:
        x, y = extra_stack.pop()
        if (x, y) in extra_visited or (x, y) in all_paths:
            continue

        extra_visited.add((x, y))
        all_paths.add((x, y))

        move_turtle(x, y)
        solver_turtle.down()

        for distance_x, distance_y in move_order:
            new_x, new_y = x + distance_x, y + distance_y
            if maze[new_y][new_x] != "#" and (new_x, new_y) not in extra_visited:
                extra_stack.append((new_x, new_y))

    print("Returning to the beginning to solve the maze in the shortest way")

    # Returning to the beginning
    backtrack_path = best_path[::-1]
    for i in range(1, len(backtrack_path)):
        x, y = backtrack_path[i]
        prev_x, prev_y = backtrack_path[i - 1]
        dx, dy = x - prev_x, y - prev_y
        while (prev_x, prev_y) != (x, y):
            move_turtle_and_rotate(prev_x, prev_y, (dx, dy))
            prev_x += dx
            prev_y += dy

    # solve the maze in the shortest way
    for i in range(1, len(best_path)):
        x, y = best_path[i]
        prev_x, prev_y = best_path[i - 1]
        dx, dy = x - prev_x, y - prev_y
        move_turtle_and_rotate(x, y, (dx, dy))

    return  best_path, list(all_paths)



def solve_maze_backtracking(maze, start, end):
    solver_turtle.speed(0)
    best_path = []
    all_paths = []
    paths = []
    move_order = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    shortest_path_length = float('inf')

    def move_turtle_back(x, y, direction):
        solver_turtle.up()
        rotate_turtle(direction)
        move_turtle(x, y)
        solver_turtle.down()

    def backtrack(x, y, path, visited):
        nonlocal best_path, shortest_path_length
        visited.add((x, y))
        path.append((x, y))

        if path:
            prev_x, prev_y = path[-2] if len(path) > 1 else (x, y)
            dx, dy = x - prev_x, y - prev_y
            move_turtle_and_rotate(x, y, (dx, dy))
        else:
            move_turtle(x, y)

        solver_turtle.down()

        if (x, y) == end:
            paths.append(list(path))
            if len(path) < shortest_path_length:
                best_path = list(path)
                shortest_path_length = len(path)
        else:
            for distance_x, distance_y in move_order:
                new_x, new_y = x + distance_x, y + distance_y
                if maze[new_y][new_x] != "#" and (new_x, new_y) not in visited:
                    backtrack(new_x, new_y, path, visited)

        
        path.pop()
        visited.remove((x, y))

        if path:
            last_x, last_y = path[-1]
            dx, dy = last_x - x, last_y - y
            move_turtle_back(last_x, last_y, (dx, dy))

    visited = set()
    backtrack(start[0], start[1], [], visited)

    print("Solving the maze in the shortest way.")

    # Sort paths by length
    paths.sort(key=len)

    # Move the turtle to the end of the best path found
    if best_path:
        for i in range(1, len(best_path)):
            x, y = best_path[i]
            prev_x, prev_y = best_path[i - 1]
            dx, dy = x - prev_x, y - prev_y
            move_turtle_and_rotate(x, y, (dx, dy))

    return best_path, paths



def rotate_turtle(direction):
        if direction == (0, -1):   # Up
            solver_turtle.setheading(90)
        elif direction == (1, 0):  # Right
            solver_turtle.setheading(0)
        elif direction == (0, 1):  # Down
            solver_turtle.setheading(270)
        elif direction == (-1, 0): # Left
            solver_turtle.setheading(180)
            
def move_turtle_and_rotate(x, y, direction):
        rotate_turtle(direction)
        move_turtle(x, y)    
    
            

if __name__ == "__main__":
    # Instantiate objects
    maze_turtle = MazeTurtle()
    solver_turtle = SolverTurtle()
    
    # Draw the Maze and set the Start and End coordinates
    start_pos, end_pos = draw_maze(maze)
    
   
    
    # Method to solve the maze with Greedy approach
    print("Solving maze in a Greedy way")
    print()
    best_path, paths = solve_maze_greedy(maze, start_pos, end_pos)    
    print()
    print("Path taken")
    print(paths)
    print(); print()
    print("Shortest path")
    print(best_path)
    print(); print()
    
    # Método para resolver el laberinto con enfoque Backtracking
    print()
    print("Solving maze in a Backtracking way")
    print()
    best_path, paths = solve_maze_backtracking(maze, start_pos, end_pos)        
    print()
    print("All solutions")
    print(paths)
    print(); print()
    print("Shortest path")
    print(best_path)
    

    wn.mainloop()
