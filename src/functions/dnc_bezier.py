# bezier yang bisa n points divide and conquer

import matplotlib.pyplot as plt
from scipy.special import comb
import numpy as np

def midpoint(points):
    npoints = len(points)
    n = npoints - 1
    coeffs = np.array([comb(n, i) for i in range(npoints)])
    result_x = np.sum(coeffs * points[:, 0]) / 2 ** n
    result_y = np.sum(coeffs * points[:, 1]) / 2 ** n
    return np.array([result_x, result_y])

def dnc_bezier_curve(points, npoints, iteration):
    if iteration == 0 or npoints == 2:
        return np.array([points[0], points[-1]])
    else:
        left_array = np.array([midpoint(points[:1])])
        right_array = np.array([midpoint(points[0:])])
        for i in range(1, npoints):
            left_array = np.append(left_array, [midpoint(points[:i+1])], axis=0)
            right_array = np.append(right_array, [midpoint(points[i:])], axis=0)

        left_curve = dnc_bezier_curve(left_array, npoints, iteration - 1)
        right_curve = dnc_bezier_curve(right_array, npoints, iteration - 1)
        
        return np.concatenate((left_curve, right_curve[1:]))