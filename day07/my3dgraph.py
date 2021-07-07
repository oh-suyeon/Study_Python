import pymysql
from astropy.table import row
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

Z = []

## 삼성 전자 price 가져와 Z축 리스트에 넣기
conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='mypydb', charset='utf8')
cur = conn.cursor()

s_code = '005930'

cur.execute("SELECT price FROM stock WHERE s_code =" + s_code)

while(True) :
    row = cur.fetchone()
    if row == None :
        break
    Z.append(row[0])
    
conn.close()

## 표 그리기
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = [0, 0, 0, 0, 0, 0]  
Y = [0, 2, 4, 6, 8, 10]

ax.plot(X, Y, Z)
plt.show()

