import pymysql

input1 = input("삭제할 행의 row01 값 입력 > ")

sql = "DELETE FROM sampk WHERE row01= " + input1

conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='mypydb', charset='utf8')
cur = conn.cursor()

#cur.execute("DELETE FROM sampk WHERE row01=3")
cur.execute(sql)

conn.commit()
conn.close()
