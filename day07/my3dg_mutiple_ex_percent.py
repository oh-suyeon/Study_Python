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
    z_n = np.array(z)
    if z_n[0] == 0 :
        continue
    z_n = z_n / z_n[0]
    
    ax.plot(x, y, z_n)


plt.show()
