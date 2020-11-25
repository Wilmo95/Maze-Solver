from pyeasyga import pyeasyga
import numpy as np

how_many_moves = 40
data_no = [{'bit': '1'}]
data = []
for i in range(how_many_moves*2):
    data.append(data_no[0])


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


population = 200
mutation = 0.05
alg = pyeasyga.GeneticAlgorithm(data, population_size= population, mutation_probability= mutation, elitism= True)
maze = create_maze()

def fitness(item, data):
    print(data)
    moves = glue(item, data)
    print(moves)


# class new_ga(pyeasyga.GeneticAlgorithm):
alg.fitness_function = fitness
alg.run()
