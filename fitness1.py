from pyeasyga import pyeasyga
from matplotlib import pyplot as plt
import time

how_many_moves = 40
data_temp = [{'bit': '1'}]
data = []
for i in range(how_many_moves*2):
    data.append(data_temp[0])


def create_maze(size = None):
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

def check_if_right(coordinates, maze):
    if maze[coordinates[0]][coordinates[1]] == 'E':
        return 0
    elif maze[coordinates[0]][coordinates[1]] == ' ':
        return 1
    else:
        return -1

# def swap(pos1, pos2, maze):
#     maze[pos1[0]][pos1[1]], maze[pos2[0]][pos2[1]] = maze[pos2[0]][pos2[1]], maze[pos1[0]][pos1[1]]
#     return maze


population = 1000
generations = 100
mutation = 0.01
alg = pyeasyga.GeneticAlgorithm(data, population_size= population, mutation_probability= mutation, elitism= True)


def fitness_1(item, data):
    maze = create_maze()
    moves = glue(item, data)
    position, end = start_end(maze)
    sum_moves = 0
    temp_position = list(position)
    for move in moves:

        if move == '10': #left
            temp_position[0] = position[0] - 1
            x = check_if_right(temp_position, maze)

            if x == 0:
                return 200-(sum(abs(a - b) for a, b in zip(position, end)))+sum_moves

            elif x == 1:
                position = list(temp_position)

            else:
                sum_moves = sum_moves - 1
                temp_position = list(position)

        elif move == '01': #right
            temp_position[0] = position[0] + 1
            x = check_if_right(temp_position, maze)

            if x == 0:
                return 200-(sum(abs(a - b) for a, b in zip(position, end)))+sum_moves

            elif x == 1:
                position = list(temp_position)

            else:
                sum_moves = sum_moves - 1
                temp_position = list(position)

        elif move == '00': #down
            temp_position[1] = position[1] + 1
            x = check_if_right(temp_position, maze)

            if x == 0:
                return 200-(sum(abs(a - b) for a, b in zip(position, end)))+sum_moves

            elif x == 1:
                position = list(temp_position)

            else:
                sum_moves = sum_moves -1
                temp_position = list(position)

        elif move == '11': #up
            temp_position[1] = position[1] - 1
            x = check_if_right(temp_position, maze)

            if x == 0:
                return 200-(sum(abs(a - b) for a, b in zip(position, end)))+sum_moves

            elif x == 1:
                position = list(temp_position)

            else:
                sum_moves = sum_moves - 1
                temp_position = list(position)

    return 100-(sum(abs(a - b) for a, b in zip(position, end)))+sum_moves

start_time = time.time()

alg.fitness_function = fitness_1
alg.create_first_generation()
alg.calculate_population_fitness()
t = []
for i in range(generations):
    alg.create_next_generation()
    t.append(alg.current_generation)
print(alg.best_individual())

value_mean = []
value = 0
value_max = []
max = 0
for generation in t:
    for i in generation:
        value = value + i.fitness
        if i.fitness > max:
            max = i.fitness

    value_mean.append(value/population)

    value_max.append(max)
    value = 0
    max = 0
print(value_mean)
print(value_max)

print(f'{time.time() - start_time} seconds')
print(f'{(time.time() - start_time)/60} minutes')

plt.plot(value_mean)
plt.plot(value_max)
plt.xlabel('Numer interacji')
plt.ylabel('Wartosc funkcji fitness1')
plt.legend(["srednia", "max"])
plt.show()