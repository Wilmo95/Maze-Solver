from pyeasyga import pyeasyga
import numpy as np


def createMaze(size = None):
        maze = []
        maze.append([1,1,1,1,1,1,1,1,1,1,1,1])
        maze.append([1,1,0,0,1,0,0,0,1,0,0,1])
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

maze = createMaze()
