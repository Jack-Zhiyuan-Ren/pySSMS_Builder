# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 15:40:45 2023

@author: zr11
"""

import numpy as np

def coordinatesOpenSim(input):
    if input.size == 0:
        output = input
    else:
        Rx = np.array([[1, 0, 0], [0, np.cos(-np.pi/2), -np.sin(-np.pi/2)], [0, np.sin(-np.pi/2), np.cos(-np.pi/2)]])
        Rzz = np.array([[np.cos(np.pi/2), -np.sin(np.pi/2), 0], [np.sin(np.pi/2), np.cos(np.pi/2), 0], [0, 0, 1]])

        R = np.dot(Rx, Rzz)
        output = np.dot(R, input.T).T

    return output
