# from functions.bf_bezier import *
# from functions.dnc_bezier import *
from functions.input_reader import *
from functions.visualize_graph import *

def pBezierASCII():
    print("""==========================================================
______          _             _____                      
| ___ \\        (_)           /  __ \\                     
| |_/ / ___ _____  ___ _ __  | /  \\/_   _ _ ____   _____ 
| ___ \\/ _ \\_  / |/ _ \\ '__| | |   | | | | '__\\ \ / / _ \\
| |_/ /  __// /| |  __/ |    | \\__/\\ |_| | |   \\ V /  __/
\\____/ \\___/___|_|\\___|_|     \\____/\\__,_|_|    \\_/ \\___|
==========================================================
          """)
    
def pMethodASCII(case):
    if case == 1:
        print("""=============================================================================================
______ _       _     _                        _   _____                 __                   
|  _  (_)     (_)   | |                      | | /  __ \               / /                   
| | | |___   ___  __| | ___    __ _ _ __   __| | | /  \/ ___  _ __    / /_ _ _   _  ___ _ __ 
| | | | \ \ / / |/ _` |/ _ \  / _` | '_ \ / _` | | |    / _ \| '_ \  / / _` | | | |/ _ \ '__|
| |/ /| |\ V /| | (_| |  __/ | (_| | | | | (_| | | \__/\ (_) | | | |/ / (_| | |_| |  __/ |   
|___/ |_| \_/ |_|\__,_|\___|  \__,_|_| |_|\__,_|  \____/\___/|_| |_/_/ \__, |\__,_|\___|_|   
                                                                          | |                
                                                                          |_|                
=============================================================================================""")
    elif case == 2:
        print("==================================================")
        print("______            _        ______  ")                    
        print("| ___ \          | |       |  ___|  ")                     
        print("| |_/ /_ __ _   _| |_ ___  | |_ ___  _ __ ___ ___ ")      
        print("| ___ \ '__| | | | __/ _ \ |  _/ _ \| '__/ __/ _ /")
        print("| |_/ / |  | |_| | ||  __/ | || (_) | | | (_|  __/")
        print("\____/|_|   \__,_|\__\___| \_| \___/|_|  \___\___|")
        print("==================================================")
         
def main():
    pBezierASCII()
    nPoints = getNPoints()

    positions = np.zeros((nPoints, 2), dtype=np.float64)
    # y_position = np.zeros(nPoints, dtype=np.float64)

    # setPoints(x_position, y_position, nPoints)
    setPoints(positions, nPoints)

    nIterations = getNIterations()

    print()

    method = getMethod()
    if method == 1 :
        pMethodASCII(1)
    else :
        pMethodASCII(2)

    animate_graph(positions, nIterations, method)

    plt.show()

if __name__ == '__main__':
    main()