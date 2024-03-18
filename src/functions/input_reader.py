import numpy as np

def getNPoints():
    while True:
        try:
            npoints = int(input("Masukkan jumlah titik yang akan digunakan: "))
            if npoints < 2:
                print("Banyaknya titik yang digunakan harus lebih dari satu!")
            else:
                return npoints
        except:
            print("Masukkan angka yang benar!")

def setPoints(x_position, y_position, npoints):
    i = 0

    while i < npoints:
        try:
            print(f"Masukkan posisi titik ke-{i+1} : ", end="")
            x_position[i], y_position[i] = map(np.float64, input().strip().split())
            i += 1
        except:
            print("Masukan posisi Anda salah (dalam format x y, contoh: 1 2)")

def getNIterations():
    while True:
        try:
            iteration = int(input("Banyak iterasi yang dilakukan: "))
            if iteration < 0:
                print("Masukkan angka bernilai positif!")
            else:
                return iteration
        except:
            print("Masukkan angka!")