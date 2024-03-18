import matplotlib.pyplot as plt
from time import time
from functions.bf_bezier import bf_bezier_curve
from functions.dnc_bezier import dnc_bezier_curve
from matplotlib.animation import FuncAnimation

def draw_graph(Positions, BezierPositions):
    plt.cla()
    plt.plot(Positions[:,0], Positions[:,1], "b--", marker="o", label="Linear equation")
    for i in range(len(Positions)):
        plt.annotate(f'({Positions[i,0]:.2f}, {Positions[i,1]:.2f})',
                    xy=(Positions[i,0], Positions[i,1]),  
                    xytext=(10, 10),  
                    textcoords='offset pixels',
                    fontsize=7)
    plt.plot(BezierPositions[:,0], BezierPositions[:,1], color="red", label="Bezier curve")
    plt.legend()
    plt.tight_layout()

def animate_graph(positions, iterations, method):
    plt.figure(num="Bezier Curve")
    if method == 1:
        plt.suptitle("Divide and Conquer Method")
        for i in range(iterations + 1):
            start = time()

            BezierPositions = dnc_bezier_curve(positions, len(positions), i)

            print(f"Waktu proses iterasi {i} = ", time() - start, " detik")

            draw_graph(positions, BezierPositions)

            plt.pause(1.5)
    # else:
    #     plt.title("Brute Force Method")
    #     for i in range(iterations + 1):
    #         start = time()

    #         xBezierPosition, yBezierPosition = bf_bezier_curve(xPos, yPos, 2 ** i + 1)

    #         print(f"Waktu proses iterasi {i} = ", time() - start, " detik")

    #         draw_graph(xPos, yPos, xBezierPosition, yBezierPosition)

    #         plt.pause(1.5)