import matplotlib.pyplot as plt
import numpy as np
import time

def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def quadratic_bezier(p0, p1, p2, iterations):
    curve = [p0]
    for _ in range(iterations):
        q0 = midpoint(p0, p1)
        q1 = midpoint(p1, p2)
        r0 = midpoint(q0, q1)
        curve.append(r0)
        p0, p1, p2 = p0, q0, r0
    curve.append(p2)  # Adding the last control point
    return curve

if __name__ == "__main__":
    # Input
    p0 = tuple(map(float, input("Enter coordinates of P0 (comma separated): ").split(",")))
    p1 = tuple(map(float, input("Enter coordinates of P1 (comma separated): ").split(",")))
    p2 = tuple(map(float, input("Enter coordinates of P2 (comma separated): ").split(",")))
    iterations = int(input("Enter number of iterations: "))

    # Start time
    start_time = time.time()

    # Generate the Bézier curve
    bezier_curve = quadratic_bezier(p0, p1, p2, iterations)

    # End time
    end_time = time.time()

    time = end_time - start_time
    # Visualization
    plt.figure()
    points = np.array(bezier_curve)
    plt.plot(points[:,0], points[:,1], marker='o', linestyle='-')
    plt.title("Quadratic Bézier Curve")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

    # Execution time
    print(f"Execution time: {time} seconds")
