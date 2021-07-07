import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from day07.mydao import DaoStock

#plt.rc('font', family='Malgun Gothic')

fig = plt.figure(figsize=(40, 40))

ax1 = fig.add_subplot(3,3,1, projection='3d')
ax2 = fig.add_subplot(3,3,2, projection='3d')
ax3 = fig.add_subplot(3,3,3, projection='3d')
ax4 = fig.add_subplot(3,3,4, projection='3d')
ax5 = fig.add_subplot(3,3,5, projection='3d')
ax6 = fig.add_subplot(3,3,6, projection='3d')
ax7 = fig.add_subplot(3,3,7, projection='3d')
ax8 = fig.add_subplot(3,3,8, projection='3d')
ax9 = fig.add_subplot(3,3,9, projection='3d')

axs = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]

ds = DaoStock()

names = ds.get_names()

Y = [0, 2, 4, 6, 8, 10]
x_ticks = []

for idx,name in enumerate(names) :
    
    X = [idx, idx, idx, idx, idx, idx]
    x_ticks.append(idx)
    
    tempZ = ds.get_prices(name) # 백분율로 만들기
    Z = [0]
    for i in range(1, 6) : 
        print(tempZ[i-1])
        if tempZ[i-1] == 0 : 
            Z.append(0)
        else :
            val = ((tempZ[i] - tempZ[i-1]) / tempZ[i-1]) * 100
            Z.append(val)
            if val > 1.5 :
                print(">>",name)
        
    axs[idx%9].plot(X, Y, Z, label=name)
    #ax.plot(X, Y, Z, label=name)


#plt.xticks(x_ticks)

plt.axis('tight')

#ax1.set_xlim(0, 1000) 
#ax.set_ylim(0, 10)
#ax.set_zlim(-100, 100)

#ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')

#plt.tight_layout()

#plt.legend()
plt.show()
