#import libraries
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
import csv
from scipy.spatial import ConvexHull
from scipy.spatial import Delaunay

def set_axes_equal(ax):
# """
# Make axes of 3D plot have equal scale so that spheres appear as spheres,
# cubes as cubes, etc.

# Input
#   ax: a matplotlib axis, e.g., as output from plt.gca().
# """

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


# Repeating all angles for every radius 




with open('femur_NewAxis.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


data1 = []
for i in range(len(data)):
    data1.append(data[i][0].split(' '))

data2 = []
for i in range(len(data1)):
    data3 = []
    for j in range(len(data1[i])):
        if data1[i][j].strip():
            data3.append(data1[i][j])
    data2.append(data3)

for i in range(len(data2)):
    for j in range(len(data2[i])):
        data2[i][j] = float(data2[i][j])

            
x = []
y = []
z = []

for i in range(len(data2)):
    x.append(np.float64(data2[i][0]))

for i in range(len(data2)):
    y.append(np.float64(data2[i][1]))

for i in range(len(data2)):
    z.append(np.float64(data2[i][2]))

x_arr = np.array(x)
y_arr = np.array(y)
z_arr = np.array(z)

#import polys
with open('polys.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


data1 = []
for i in range(len(data)):
    data1.append(data[i][0].split(' '))

data2 = []
for i in range(len(data1)):
    data3 = []
    for j in range(len(data1[i])):
        if data1[i][j].strip():
            data3.append(data1[i][j])
    data2.append(data3)

for i in range(len(data2)):
    for j in range(len(data2[i])):
        data2[i][j] = float(data2[i][j])
polys = data2

polys_x = []
polys_y = []
polys_z = []

for i in range(len(polys)):
    polys_x.append(np.float64(polys[i][0]))

for i in range(len(polys)):
    polys_y.append(np.float64(polys[i][1]))

for i in range(len(polys)):
    polys_z.append(np.float64(polys[i][2]))
##



data4 = np.column_stack((x_arr,y_arr,z_arr))
data5 = np.column_stack((polys_x,polys_y,polys_z))
#print(data4)
# Creating figure
fig = plt.figure(figsize =(32, 18)) 
ax = plt.axes(projection ='3d') 
 
# Creating color map
my_cmap = plt.get_cmap('hot')



# print("hull.vertices")
# print(hull.vertices)
# print("hull.simplices")
# print(hull.simplices)

# print("data4[hull.vertices, 0]")
# print(data4[hull.vertices, 0])
# print("stop")




#print(triangles)


##modifying triangles with 455 to 456
for i in range(len(data5)):
    for j in range(len(data5[i])):
        data5[i][j] = data5[i][j] - 1
print(data5)
#print(triangles)
##

# Creating plot
ax.plot(x_arr,y_arr, z_arr, 'bo', ms = 2)
# ax.plot(polys_x ,
#         polys_y,
#         polys_z, 'ko', markersize=4)

trisurf = ax.plot_trisurf(x_arr, y_arr, z_arr,
                         triangles = data5,
                         cmap = 'viridis', 
                         alpha = 0.2,
                         edgecolor = 'k') 

#fig.colorbar(trisurf, ax = ax, shrink = 0.5, aspect = 5)
ax.set_title('Tri-Surface plot')
#print(x_arr)
# Adding labels
ax.set_xlabel('X-axis', fontweight ='bold')
ax.set_ylabel('Y-axis', fontweight ='bold')
ax.set_zlabel('Z-axis', fontweight ='bold')
set_axes_equal(ax)    
#show plot
# plt.show()