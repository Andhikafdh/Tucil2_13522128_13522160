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

def setPoints(position, npoints):
    i = 0

    while i < npoints:
        try:
            print(f"Masukkan posisi titik ke-{i+1} : ", end="")
            current_point = np.array(list(map(np.float64, input().strip().split())))
            if len(current_point) != 2:
                raise Exception
            position[i] = current_point
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

def getMethod():
    while True:
        print("|==== Metode yang dapat dipilih ====|")
        print("| 1. Divide and Conquer             |")
        print("| 2. Brute-force                    |")
        print("|===================================|\n")
        try:
            method = int(input("Metode penyelesaian yang dipilih: \n"))
            if method != 1 and method != 2:
                print("Masukkan angka sesuai dengan penomoran metode!")
            else:
                return method
        except:
            print("Masukkan angka!")