from pyeasyga import pyeasyga
import numpy as np

how_many_moves = 40
data_temp = [{'bit': '1'}]
data = []
for i in range(how_many_moves*2):
    data.append(data_temp[0])


def create_maze(size = None):
    maze = []
    maze.append(['#','#','#','#','#','#','#','#','#','#','#','#'])
    maze.append(['#','S',' ','#',' ',' ',' ','#',' ',' ',' ','#'])
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

def glue(chosen, bits):

    moves_temp = []
    moves = []
    for i in chosen:
        if i:
            moves_temp.append(bits[0].get('bit'))
        else:
            moves_temp.append('0')
    for ele in range(0, len(moves_temp), 2):
        moves.append(moves_temp[ele] + moves_temp[ele+1])

    return moves

def start_end(maze):
    start = []
    end = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = [i,j]
            if maze[i][j] == 'E':
                end = [i,j]

    return start, end

def chech_if_right(coordinates, maze):
    if maze[coordinates[0]][coordinates[1]] == 'E':
        return 0
    elif maze[coordinates[0]][coordinates[1]] == ' ':
        return 1
    else:
        return -1

# def swap(pos1, pos2, maze):
#     maze[pos1[0]][pos1[1]], maze[pos2[0]][pos2[1]] = maze[pos2[0]][pos2[1]], maze[pos1[0]][pos1[1]]
#     return maze


population = 200
mutation = 0.05
alg = pyeasyga.GeneticAlgorithm(data, population_size= population, mutation_probability= mutation, elitism= True)


def fitness(item, data):
    maze = create_maze()
    moves = glue(item, data)
    position, end = start_end(maze)
    sum_moves = 0
    temp_position = list(position)
    for move in moves:

        if move == '10': #left
            temp_position[0] = position[0] - 1
            x = chech_if_right(temp_position, maze)

            if x == 0:
                return -(sum(abs(a - b) for a, b in zip(position, end)))+sum_moves

            elif x == 1:
                position = list(temp_position)

            else:
                sum_moves = sum_moves - 1
                temp_position = list(position)

        elif move == '01': #right
            temp_position[0] = position[0] + 1
            x = chech_if_right(temp_position, maze)

            if x == 0:
                return -(sum(abs(a - b) for a, b in zip(position, end)))+sum_moves

            elif x == 1:
                position = list(temp_position)

            else:
                sum_moves = sum_moves - 1
                temp_position = list(position)

        elif move == '00': #up
            temp_position[1] = position[1] - 1
            x = chech_if_right(temp_position, maze)

            if x == 0:
                return -(sum(abs(a - b) for a, b in zip(position, end)))+sum_moves

            elif x == 1:
                position = list(temp_position)

            else:
                sum_moves = sum_moves -1
                temp_position = list(position)

        elif move == '11': #down
            temp_position[1] = position[1] + 1
            x = chech_if_right(temp_position, maze)

            if x == 0:
                return -(sum(abs(a - b) for a, b in zip(position, end)))+sum_moves

            elif x == 1:
                position = list(temp_position)

            else:
                sum_moves = sum_moves - 1
                temp_position = list(position)

    return -(sum(abs(a - b) for a, b in zip(position, end)))+sum_moves

# class new_ga(pyeasyga.GeneticAlgorithm):
alg.fitness_function = fitness
alg.run()
print(alg.best_individual())