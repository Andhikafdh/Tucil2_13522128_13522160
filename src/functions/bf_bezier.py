import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb
import time

def compute_bezier_curve(n, i, t):
    curvePoint = comb(n,i) * t ** i * (1 - t) ** (n - i)
    return curvePoint

def bezier_curve(x, y, cell_amount):
    t = np.linspace(0,1,cell_amount)
    n = len(x)

    array = np.array([compute_bezier_curve(n - 1, i, t) for i in range(0, n)], dtype=np.float64)

    xBezier = np.dot(x, array)
    yBezier = np.dot(y, array)

    return xBezier, yBezier

while True:
    try:
        nTitik = int(input("Masukkan jumlah titik yang akan digunakan: "))
        if nTitik < 2:
            print("Banyaknya titik yang digunakan harus lebih dari satu!")
        else:
            break
    except:
        print("Masukkan angka dengan benar!")

xPos = np.zeros(nTitik, dtype=np.float64)
yPos = np.zeros(nTitik, dtype=np.float64)

i = 0

while i < nTitik:
    try:
        print(f"Masukkan posisi titik ke-{i} (format: x,y) : ", end="")
        xPos[i], yPos[i] = map(np.float64, input().strip().split(","))
        i += 1
    except:
        print("Masukan posisi dengan benar!")

iterations = None

while True:
    try:
        iterations = int(input("Banyak iterasi yang dilakukan: "))
        if iterations < 0:
            print("Masukkan angka yang bernilai positif!")
        else:
            break
    except:
        print("Masukkan angka dengan benar!")

start = time.time()

cells = 2 ** iterations + 1

xBezierPosition, yBezierPosition = bezier_curve(xPos, yPos, cells)

print(time.time() - start)

plt.plot(xPos, yPos, "--", marker="o", label="Linear equation")
plt.plot(xBezierPosition, yBezierPosition,  marker="o", color="red", label="Bezier curve")
plt.legend()
plt.tight_layout()
plt.show()




