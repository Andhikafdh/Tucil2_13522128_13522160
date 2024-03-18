# from functions.bf_bezier import *
# from functions.dnc_bezier import *
from functions.input_reader import *
from functions.visualize_graph_copy import *

def pBezierASCII():
    print("""
______          _             _____                      
| ___ \\        (_)           /  __ \\                     
| |_/ / ___ _____  ___ _ __  | /  \\/_   _ _ ____   _____ 
| ___ \\/ _ \\_  / |/ _ \\ '__| | |   | | | | '__\\ \ / / _ \\
| |_/ /  __// /| |  __/ |    | \\__/\\ |_| | |   \\ V /  __/
\\____/ \\___/___|_|\\___|_|     \\____/\\__,_|_|    \\_/ \\___|
============================================================
          """)

def main():
    pBezierASCII()
    nPoints = getNPoints()

    positions = np.zeros((nPoints, 2), dtype=np.float64)
    # y_position = np.zeros(nPoints, dtype=np.float64)

    # setPoints(x_position, y_position, nPoints)
    setPoints(positions, nPoints)

    nIterations = getNIterations()

    method = getMethod()

    animate_graph(positions, nIterations, method)

if __name__ == '__main__':
    main()