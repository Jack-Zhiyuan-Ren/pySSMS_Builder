# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 14:17:34 2023

@author: zr11
"""

import numpy as np
points = np.array([[5,0,0],[1, 1, 3],[0, 0, 0],[5,5,5],[0, 1.1, 1.2], [1, 2.2, 3]])

from scipy.spatial import Delaunay
tri = Delaunay(points)



import matplotlib.pyplot as plt



fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(points[:,0], points[:,1], points[:,2],triangles=Delaunay(points[:,:]).simplices)
plt.show()