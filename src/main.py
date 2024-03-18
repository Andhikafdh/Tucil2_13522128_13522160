from functions.brute_bezier import *
from functions.dnc_bezier import *
from functions.input_reader import *
from functions.visualize_graph import *

def main():
    nPoints = getNPoints()

    x_position = np.zeros(nPoints, dtype=np.float64)
    y_position = np.zeros(nPoints, dtype=np.float64)

    setPoints(x_position, y_position, nPoints)

    nIterations = getNIterations()

    sleep_time = 2

    

if __name__ == '__main__':
    main()