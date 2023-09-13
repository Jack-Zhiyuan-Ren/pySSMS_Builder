import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D
import csv

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

print(data2)



triangles = data2

triang = mtri.Triangulation(x_arr, y_arr, z , triangles=triangles)

z = [0.1,0.2,0.3,0.4]

fig, ax = plt.subplots(subplot_kw =dict(projection="3d"))
ax.plot_trisurf(triang, z)

plt.show()