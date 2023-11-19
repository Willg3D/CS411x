# William Glass
# CS 411x Algorithms
# HW 5
# 2023-11-20

import matplotlib.pyplot as plt # used for ploting points
from tkinter.simpledialog import askinteger # askinteger from tkinter for dialog box
import numpy as np # used for generating random points
import time # used for timing quickHull

# finds if point is on clockwise (right) side or
# counterclockwise (left) side of a line between points a and b
# returns 0 if collinear, 1 if clockwise, and 2 if counterclockwise
def findSidePoint(a, b, c):
    val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    if val == 0:
        return 0  # Collinear
    if val > 0:
        return 1  # Clockwise
    return 2  # Counterclockwise

# Calulates a single point's (c) distance from a line
# created form  two points (a and b)
def distanceFromLine(a, b, c):
    aCoef = b[1] - a[1]
    bCoef = a[0] - b[0]
    cCoef = (b[0] - a[0]) * a[1] - (b[1] - a[1]) * a[0]
    
    return abs((aCoef*c[0])+(bCoef*c[1])+cCoef) / ((aCoef**2) + (bCoef**2))**0.5

# Computes the convex hull of a set of 2D points using the QuickHull algorithm.
def quickHull(points):    
    # Recursive helper function to find points on the convex hull
    def recursiveHull(a, b, convexHull, points):
        if not points:
            return

        # Find the farthest point from the line formed by points a and b
        c = max(points, key=lambda point: distanceFromLine(a, b, point))
        
        # Insert the new point between points a and b in convexHull
        indexB = convexHull.index(b)
        convexHull.insert(indexB, c)

        # Recursively find points on the left side of line ac
        leftSidePoints = [point for point in points if findSidePoint(a, c, point) == 2]
        recursiveHull(a, c, convexHull, leftSidePoints)

        # Recursively find points on the left side of line cb
        rightSidePoints = [point for point in points if findSidePoint(c, b, point) == 2]
        recursiveHull(c, b, convexHull, rightSidePoints)

    # Finding left (a) and right (b) most points
    a = min(points, key=lambda point: point[0])
    b = max(points, key=lambda point: point[0])
    convexHull = [a, b]

    # Recursively find points on the left side of line ab
    leftSidePoints = [point for point in points if findSidePoint(a, b, point) == 2]
    recursiveHull(a, b, convexHull, leftSidePoints)

    # Recursively find points on the right side of line ab
    rightSidePoints = [point for point in points if findSidePoint(a, b, point) == 1]
    recursiveHull(b, a, convexHull, rightSidePoints)

    return convexHull


def plotConvexHull(points, convexHull):
    convexHull.append(convexHull[0])  # Add the first point to the end to close the loop
    convexHull = list(map(tuple, convexHull))  # Convert the list of lists to a list of tuples
    plt.plot(*zip(*convexHull), color='red')


def plotRandomPoints(points, numPoints, elapsed_time, convexHullLength):
    plt.scatter(points[:, 0], points[:, 1], color='blue')
    plt.title(f"Random Generated Points: {numPoints} points\
              \nQuickHull Points: {convexHullLength}\
              \nCompute Time: {elapsed_time:.6f} seconds")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

while True:
    numPoints = askinteger("Input", "Enter the number of points (3 or More Positive Ints):")
    if numPoints is None:
        break
    if numPoints > 2:
        #np.random.seed(5)
        points = np.random.rand(numPoints, 2) # generates points (x,y) from 0 to 1
        pointsForConvexHull = points.tolist() # tolist() used to use index()
        
        start_time = time.time()
        convexHull = quickHull(pointsForConvexHull)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # Print information about the computation
        print(f"QuickHull Compute Time: {elapsed_time:.6f} seconds")
        print("Total Points: ", numPoints)
        print("Quickhull Points: ", len(convexHull))
        
        # Plot the random points, convex hull, and display the plot
        plotRandomPoints(points, numPoints, elapsed_time, len(convexHull))
        plotConvexHull(points, convexHull)
        plt.show()
        break
