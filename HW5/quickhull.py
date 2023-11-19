# William Glass
# CS 411x Algorithms
# HW 5
# 2023-11-20

import matplotlib.pyplot as plt # used for ploting points
from tkinter.simpledialog import askinteger  # askinteger from tkinter for dialog box

import numpy as np # used for generating random points


# finds if point is on clockwise (right) side or
# counterclockwise (left) side of a line between points a and b
# returns 0 if collinear, 1 if clockwise, and 2 if counterclockwise
def findSidePoint(a, b, c):
    val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    if val == 0:
        return 0  # Collinear
    if val > 0: # clockwise
        return 1
    return 2 # counterclockwise

def distanceFromLine(a, b, c):
    aCoef = b[1] - a[1]
    bCoef = a[0] - b[0]
    cCoef = (b[0] - a[0]) * a[1] - (b[1] - a[1]) * a[0]
    
    return abs((aCoef*c[0])+(bCoef*c[1])+cCoef) / ((aCoef**2) + (bCoef**2))**0.5

def quickHull(points):
    # Recursive helper function to find points on the convex hull
    def recursiveHull(a, b, convexHull, points):
        if not points:
            return

    #finding left (a) and right (b) most points
    a = min(points, key=lambda point: point[0])
    b = max(points, key=lambda point: point[0])

    leftSidePoints = [point for point in points if findSidePoint(a, b, point) == 2]
    recursiveHull()
    rightSidePoints = [point for point in points if findSidePoint(a, b, point) == 2]


    convexHull = [a, b]


    return convexHull


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
        convexhull = quickHull(points)
        print("quickhull points: ", convexhull)
        plotRandomPoints(points)
        break