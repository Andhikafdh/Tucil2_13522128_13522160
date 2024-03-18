import matplotlib.pyplot as plt
from scipy.special import comb
import numpy as np
from time import time

def bernstein_polynomial(N: int, i: int, t: np.float64):
    return comb(N,i) * t ** i * (1 - t) ** (N - i)

def bezier_curve(x_pos, y_pos, cell_amount: np.int64):
    t = np.linspace(0,1,cell_amount)
    n = len(x_pos)

    polynomial_array = np.array([bernstein_polynomial(n - 1, i, t) for i in range(0, n)], dtype=np.float64)

    x_bpos = np.dot(x_pos, polynomial_array)
    y_bpos = np.dot(y_pos, polynomial_array)

    return x_bpos, y_bpos

while True:
    try:
        points = int(input("Masukkan jumlah titik yang akan digunakan: "))
        if points < 2:
            print("Banyaknya titik yang digunakan harus lebih dari satu!")
        else:
            break
    except:
        print("Masukkan angka yang benar!")

x_position = np.zeros(points, dtype=np.float64)
y_position = np.zeros(points, dtype=np.float64)

i = 0

while i < points:
    try:
        print(f"Masukkan posisi titik P{i} : ", end="")
        x_position[i], y_position[i] = map(np.float64, input().strip().split(","))
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

cells = 2 ** iteration + 1

x_bezier_position, y_bezier_position = bezier_curve(x_position, y_position, cells)

print(time() - start)

plt.plot(x_position, y_position, "--", marker="o", label="Linear equation")
plt.plot(x_bezier_position, y_bezier_position,  marker="o", color="red", label="Bezier curve")

plt.legend()

plt.tight_layout()

plt.show()