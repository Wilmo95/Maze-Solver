from pyeasyga import pyeasyga
import numpy as np

data_no = [{'direction': 'left'},
        {'direction': 'right'},
        {'direction': 'up' },
        {'direction': 'down' }]
data = []
for i in range(10):
        data.append(data_no[0])
        data.append(data_no[1])
        data.append(data_no[2])
        data.append(data_no[3])
print(data)
def createMaze(size = None):
        maze = []
        maze.append([1,1,1,1,1,1,1,1,1,1,1,1])
        maze.append([1,'S',0,0,1,0,0,0,1,0,0,1])
        maze.append([1,1,1,0,0,0,1,0,1,1,0,1])
        maze.append([1,0,0,0,1,0,1,0,0,0,0,1])
        maze.append([1,0,1,0,1,1,0,0,1,1,0,1])
        maze.append([1,0,0,1,1,0,0,0,1,0,0,1])
        maze.append([1,0,0,0,0,0,1,0,0,0,1,1])
        maze.append([1,0,1,0,0,1,1,0,1,0,0,1])
        maze.append([1,0,1,1,1,0,0,0,1,1,0,1])
        maze.append([1,0,1,0,1,1,0,1,0,1,0,1])
        maze.append([1,0,1,0,0,0,0,0,0,0,'E',1])
        maze.append([1,1,1,1,1,1,1,1,1,1,1,1])

        return maze

population = 200
mutation = 0.05
alg = pyeasyga.GeneticAlgorithm(data, population_size= population, mutation_probability= mutation, elitism= True)
maze = createMaze()

def fitness(item , data):
        distance = None
        for chosen, dir in zip(item, data):
                if chosen:
                       move = dir.get('direction')
                       if move == 'left'

# class new_ga(pyeasyga.GeneticAlgorithm):
alg.fitness_function = fitness
alg.run()
