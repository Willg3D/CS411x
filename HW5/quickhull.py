# William Glass
# CS 411x Algorithms
# HW 5
# 2023-11-20

import matplotlib.pyplot as plt
import numpy as np

def plotRandomPoints(numPoints):
    #np.random.seed(0)
    points = np.random.rand(numPoints, 2)
    
    plt.scatter(points[:, 0], points[:, 1], color='blue')
    plt.title(f'Random Generated Points - {numPoints} points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

numPoints = 20
plotRandomPoints(numPoints)
