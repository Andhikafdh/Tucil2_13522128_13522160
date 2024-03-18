# bezier yang bisa n points divide and conquer

import matplotlib.pyplot as plt
from scipy.special import comb
import numpy as np
from time import time

def midpoint(points):
    result = 0
    npoints = len(points)
    n = npoints - 1
    for i in range(npoints):
        result += comb(n,i) * points[i]
    return result / 2 ** n

def bezier_curve(points, npoints, iteration):
    if iteration == 0 or npoints == 2:
        return np.array([points[0], points[-1]])
    else:
        left_array = np.array([])
        right_array = np.array([])
        for i in range(npoints):
            left_array = np.append(left_array, midpoint(points[:i+1]))
            right_array = np.append(right_array, midpoint(points[i:]))

        left_curve = bezier_curve(left_array, npoints, iteration - 1)
        right_curve = bezier_curve(right_array, npoints, iteration - 1)
        return np.concatenate((left_curve, right_curve[1:]))
    
if __name__ == '__main__':
    
    while True:
        try:
            npoints = int(input("Masukkan jumlah titik yang akan digunakan: "))
            if npoints < 2:
                print("Banyaknya titik yang digunakan harus lebih dari satu!")
            else:
                break
        except:
            print("Masukkan angka yang benar!")

    x_position = np.zeros(npoints, dtype=np.float64)
    y_position = np.zeros(npoints, dtype=np.float64)

    i = 0

    while i < npoints:
        try:
            print(f"Masukkan posisi titik ke-{i+1} : ", end="")
            x_position[i], y_position[i] = map(np.float64, input().strip().split())
            i += 1
        except:
            print("Masukan posisi Anda salah (dalam format x y, contoh: 1 2)")

    iteration = None

    while True:
        try:
            iteration = int(input("Banyak iterasi yang dilakukan: "))
            if iteration < 0:
                print("Masukkan angka bernilai positif!")
            else:
                break
        except:
            print("Masukkan angka!")

    start = time()

    x_bezier_position = bezier_curve(x_position, npoints, iteration)
    y_bezier_position = bezier_curve(y_position, npoints, iteration)

    print(time() - start)

    plt.figure(num="Bezier Curve Divide and Conquer n Points")

    plt.title("Bezier curve using divide and conquer")

    plt.plot(x_position, y_position, "--", marker=".", label="Linear equation")
    plt.plot(x_bezier_position, y_bezier_position, color="red", label="Bezier curve")

    plt.legend()

    plt.tight_layout()

    plt.show()