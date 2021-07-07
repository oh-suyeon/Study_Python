import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from day07.mydao import DaoStock

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ds = DaoStock()
names = ds.get_names()

Y = [0, 2, 4, 6, 8, 10]

for idx,name in enumerate(names) :
    
    X = [idx, idx, idx, idx, idx, idx]
    
    tempZ = ds.get_prices(name) 
    Z = [0]
    
    for i in range(1, 6) : 
        if tempZ[i-1] == 0 : 
            Z.append(0)
        else :
            val = ((tempZ[i] - tempZ[i-1]) / tempZ[i-1]) * 100
            Z.append(val)
            
    ax.plot(X, Y, Z, label=name)


plt.axis('tight')

plt.show()
