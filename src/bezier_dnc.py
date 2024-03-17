# bezier kuadratik divide and conquer

import matplotlib.pyplot as plt
import numpy as np
from time import time

def q_bezier_dnc(left, mid, right, iteration):
    if iteration == 0:
        return np.array([left,right], dtype=np.float64)
    else:
        left_curve = q_bezier_dnc(left, np.average([left, mid]), np.average([np.average([left, mid]), np.average([mid, right])]), iteration - 1)
        right_curve = q_bezier_dnc(np.average([np.average([left, mid]), np.average([mid, right])]), np.average([mid, right]), right, iteration - 1)
        return np.concatenate((left_curve, right_curve[1:]))
    

    
points = 3

x_position = np.zeros(points, dtype=np.float64)
y_position = np.zeros(points, dtype=np.float64)

i = 0

while i < points:
    try:
        print(f"Masukkan posisi titik ke-{i+1} : ", end="")
        x_position[i], y_position[i] = map(np.float64, input().strip().split())
        i += 1
    except:
        print("Masukan posisi Anda salah")

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

x_bezier_position = q_bezier_dnc(x_position[0], x_position[1], x_position[2], iteration)
y_bezier_position = q_bezier_dnc(y_position[0], y_position[1], y_position[2], iteration)

print(time() - start)

plt.plot(x_position, y_position, "--", marker=".", label="Linear equation")
plt.plot(x_bezier_position, y_bezier_position, color="red", label="Bezier curve")

plt.legend()

plt.tight_layout()

plt.show()