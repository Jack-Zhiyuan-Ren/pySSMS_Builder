import numpy as np

def coordinatesCorrection(input):
    if len(input) == 0:
        output = input
    else:
        Rx = np.array([[1, 0, 0], [0, np.cos(np.pi/2), -np.sin(np.pi/2)], [0, np.sin(np.pi/2), np.cos(np.pi/2)]])
        Rzz = np.array([[np.cos(-np.pi/2), -np.sin(-np.pi/2), 0], [np.sin(-np.pi/2), np.cos(-np.pi/2), 0], [0, 0, 1]])

        R = np.matmul(Rzz, Rx)
        # print(R)
        # print(np.transpose(input))
        output = np.transpose(np.matmul(R, np.transpose(input)))


    return output