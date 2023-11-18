# William Glass
# CS 411x Algorithms
# HW 5
# 2023-11-20

import matplotlib.pyplot as plt # used for ploting points
from tkinter.simpledialog import askinteger  # askinteger from tkinter for dialog box

import numpy as np # used for generating random points

def plotRandomPoints(numPoints):
    #np.random.seed(0)
    points = np.random.rand(numPoints, 2) # generates points (x,y) from 0 to 1
    
    plt.scatter(points[:, 0], points[:, 1], color='blue')
    plt.title(f'Random Generated Points - {numPoints} points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

while(True):
    numPoints = askinteger("Input", "Enter the number of points (Positive Ints Only):")
    if numPoints is None:
        break
    if numPoints > 0:
        plotRandomPoints(numPoints)
        break