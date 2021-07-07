import pymysql

data1 = ""
data2 = ""
data3 = ""

row = None

conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='mypydb', charset='utf8')
cur = conn.cursor()

cur.execute("SELECT * FROM sampk")

print("row01    row02    row03")
print("-----------------------")

while(True) :
    row = cur.fetchone()
    if row == None :
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    print('{}        {}        {}'.format(data1, data2, data3))
    
conn.close()