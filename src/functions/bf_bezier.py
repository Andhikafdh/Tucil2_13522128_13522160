import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb

def compute_bezier_curve(n, i, t):
    curvePoint = comb(n,i) * t ** i * (1 - t) ** (n - i)
    return curvePoint

def bf_bezier_curve(x, y, cell_amount):
    t = np.linspace(0,1,cell_amount)
    n = len(x)

    array = np.array([compute_bezier_curve(n - 1, i, t) for i in range(0, n)], dtype=np.float64)

    xBezier = np.dot(x, array)
    yBezier = np.dot(y, array)

    return xBezier, yBezier