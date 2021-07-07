import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from day07.mydao import DaoStock

ds = DaoStock()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X1 = [0, 0, 0, 0, 0, 0]  
Y = [0, 2, 4, 6, 8, 10] 
Z1 = ds.get_prices('삼성전자')

X2 = [2, 2, 2, 2, 2, 2]  
Z2 = ds.get_prices('LG')

X3 = [-2, -2, -2, -2, -2, -2]  
Z3 = ds.get_prices('기아')

ax.plot(X1, Y, Z1)
ax.plot(X2, Y, Z2)
ax.plot(X3, Y, Z3)

ax.set_xlim(-5, 5) 
ax.set_ylim(0, 10)
ax.set_zlim(50000, 150000)
 
plt.show()
