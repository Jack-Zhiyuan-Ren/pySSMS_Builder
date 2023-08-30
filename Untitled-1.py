
# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
 
# Creating dataset
z = np.linspace(0, 50000, 100)
x = np.sin(z)
y = np.cos(z)
 
# Creating figure
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
 
# Creating plot
ax.plot_trisurf(x, y, z,
                linewidth = 0.2,
                antialiased = True);
 
# show plot
plt.show()