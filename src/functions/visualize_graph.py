import matplotlib.pyplot as plt
from time import time
from functions.bf_bezier import bf_bezier_curve
from functions.dnc_bezier import dnc_bezier_curve
from matplotlib.animation import FuncAnimation

def draw_graph(xPos, yPos, xBezierPosition, yBezierPosition):
    plt.cla()
    plt.plot(xPos, yPos, "b--", marker="o", label="Linear equation")
    plt.plot(xBezierPosition, yBezierPosition, color="red", label="Bezier curve")
    plt.legend()
    plt.tight_layout()
    plt.show()

def animate_graph(positions, iterations, method):
    plt.figure(num="Bezier Curve")
    if method == 1:
        plt.title("Divide and Conquer Method")
        for i in range(iterations + 1):
            start = time()

            xBezierPosition = dnc_bezier_curve(xPos, len(xPos), i)
            yBezierPosition = dnc_bezier_curve(yPos, len(yPos), i)

            print(f"Waktu proses iterasi {i} = ", time() - start, " detik")

            draw_graph(xPos, yPos, xBezierPosition, yBezierPosition)

            plt.pause(1.5)
    # else:
    #     plt.title("Brute Force Method")
    #     for i in range(iterations + 1):
    #         start = time()

    #         xBezierPosition, yBezierPosition = bf_bezier_curve(xPos, yPos, 2 ** i + 1)

    #         print(f"Waktu proses iterasi {i} = ", time() - start, " detik")

    #         draw_graph(xPos, yPos, xBezierPosition, yBezierPosition)

    #         plt.pause(1.5)