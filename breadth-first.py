import queue
import time


def create_maze():
    maze = []
    maze.append(['#','#','#','#','#','#','#','#','#','#','#','#'])
    maze.append(['#','S',' ',' ','#',' ',' ',' ','#',' ',' ','#'])
    maze.append(['#','#','#',' ',' ',' ','#',' ','#','#',' ','#',])
    maze.append(['#',' ',' ',' ','#',' ','#',' ',' ',' ',' ','#',])
    maze.append(['#',' ','#',' ','#','#',' ',' ','#','#',' ','#',])
    maze.append(['#',' ',' ','#','#',' ',' ',' ','#',' ',' ','#',])
    maze.append(['#',' ',' ',' ',' ',' ','#',' ',' ',' ','#','#',])
    maze.append(['#',' ','#',' ',' ','#','#',' ','#',' ',' ','#',])
    maze.append(['#',' ','#','#','#',' ',' ',' ','#','#',' ','#',])
    maze.append(['#',' ','#',' ','#','#',' ','#',' ','#',' ','#',])
    maze.append(['#',' ','#',' ',' ',' ',' ',' ',' ',' ','E','#'])
    maze.append(['#','#','#','#','#','#','#','#','#','#','#','#'])

    return maze


def print_maze(maze, path=""):
    for j in range(len(maze)):
        for x, pos in enumerate(maze[j]):
            if pos == 'S':
                startx = x
                starty = j
    i = startx
    j = starty
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def check_if_right(maze, moves):
    for j in range(len(maze)):
        for x, pos in enumerate(maze[j]):
            if pos == 'S':
                startx = x
                starty = j
    i = startx
    j = starty
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def find_end(maze, moves):
    for j in range(len(maze)):
        for x, pos in enumerate(maze[j]):
            if pos == 'S':
                startx = x
                starty = j
    i = startx
    j = starty
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "E":
        print("Found: " + moves)
        print_maze(maze, moves)
        return True

    return False



my_queue = queue.Queue()
my_queue.put("")
add = ""
maze = create_maze()
start_time = time.time()

while not find_end(maze, add):
    add = my_queue.get()
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if check_if_right(maze, put):
            my_queue.put(put)
print(f'{time.time() - start_time} seconds ')
print(f'{(time.time() - start_time)/60} minutes')