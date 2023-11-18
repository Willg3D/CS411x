# William Glass
# CS 411x Algorithms
# HW 5
# 2023-11-20

import matplotlib.pyplot as plt # used for ploting points
from tkinter.simpledialog import askinteger  # askinteger from tkinter for dialog box

import numpy as np # used for generating random points




def quickHull(points):

    #finding left (a) and right (b) most points
    a = min(points, key=lambda point: point[0])
    b = max(points, key=lambda point: point[0])

    convexHull = [a, b]


    return convexHull

# Recursive helper function to find points on the convex hull
def recursiveHull(a, b, convexHull, points):
    pass

def plotRandomPoints(points):
    
    plt.scatter(points[:, 0], points[:, 1], color='blue')
    plt.title(f'Random Generated Points - {numPoints} points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

while(True):
    numPoints = askinteger("Input", "Enter the number of points (3 or More Positive Ints):")
    if numPoints is None:
        break
    if numPoints > 2:
        np.random.seed(0)
        points = np.random.rand(numPoints, 2) # generates points (x,y) from 0 to 1
        print(quickHull(points))
        plotRandomPoints(points)
        break