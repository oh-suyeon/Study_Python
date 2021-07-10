import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from stock.stock_dao import StockDao

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

sd = StockDao()

s_names = sd.get_names();
cnt_days = sd.count_days()

for idx, s_name in enumerate(s_names):
    x = np.zeros((cnt_days)) + idx
    y = range(cnt_days)
    
    z = sd.get_price(s_name)
    z_n = np.array(z)
    
    if z_n[0] == 0 :
        print(s_name)
        continue
    
    z_n = z_n / z_n[0]
    
    ax.plot(x,y,z_n)

plt.show()