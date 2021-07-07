
# Standard import
import matplotlib.pyplot as plt
# Import 3D Axes 
from mpl_toolkits.mplot3d import axes3d
# Set up Figure and 3D Axes 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Get some 3D data
X = [0, 0, 0, 0, 0, 0]  
Y = [0, 2, 4, 6, 8, 10] # 시간
Z = [0, 3, 0, 6, 5, 3] # price
# Plot using Axes notation and standard function calls
ax.plot(X, Y, Z)
plt.show()
