# bezier yang bisa n points divide and conquer

import matplotlib.pyplot as plt
from scipy.special import comb
import numpy as np

def midpoint(points):
    result = 0
    npoints = len(points)
    n = npoints - 1
    for i in range(npoints):
        result += comb(n,i) * points[i]
    return result / 2 ** n

def dnc_bezier_curve(points, npoints, iterations):
    curves = [points]
    for iteration in range(iterations):
        left_array = np.array([])
        right_array = np.array([])
        for i in range(npoints):
            left_array = np.append(left_array, midpoint(points[:i+1]))
            right_array = np.append(right_array, midpoint(points[i:]))
        points = np.concatenate((left_array, right_array[1:]))
        curves.append(points)
    return curves