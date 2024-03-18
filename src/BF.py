import matplotlib.pyplot as plt
import numpy as np
import time

def compute_bezier_curve(P0, P1, P2, t):
    B_t = (1 - t)**2 * P0 + 2 * (1 - t) * t * P1 + t**2 * P2
    return B_t

def bezier_curve(P0, P1, P2, iterations):
    curve_points = [P0]
    
    for i in range(iterations):
        t = i / iterations
        B_t = compute_bezier_curve(P0, P1, P2, t)
        curve_points.append(B_t)
    
    curve_points.append(P2)  
    
    curve_points = np.array(curve_points)
    
    # Menampilkan kurva Bézier
    plt.plot(curve_points[:, 0], curve_points[:, 1], marker='o')
    plt.title('Bézier Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def main():
    x0, y0 = map(float, input("Masukkan koordinat X dan Y untuk titik awal (P0): ").split(","))
    x1, y1 = map(float, input("Masukkan koordinat X dan Y untuk titik kontrol antara (P1): ").split(","))
    x2, y2 = map(float, input("Masukkan koordinat X dan Y untuk titik akhir (P2): ").split(","))
    iterations = int(input("Masukkan jumlah iterasi: "))
    
    start_time = time.time()
    
    bezier_curve(np.array([x0, y0]), np.array([x1, y1]), np.array([x2, y2]), iterations)
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Waktu eksekusi program: {execution_time:.5f} detik")

if __name__ == "__main__":
    main()
