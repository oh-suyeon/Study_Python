import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from day07.mydao import DaoStock
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ds = DaoStock()
names = ds.get_names()

for idx,name in enumerate(names) :
    
    x = np.zeros((6)) + idx
    y = range(6)
    z = ds.get_prices(name)
    
    ax.plot(x, y, z)


plt.show()
