import pymysql

input1 = input("변경할 row02 값 입력 > ")
input2 = input("변경할 row03 값 입력 > ")
input3 = input("변경할 행의 row01 값 입력 > ")

sql = "UPDATE sampk SET " + "row02='{}', row03='{}' WHERE row01={}".format(input1, input2, input3)

conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='mypydb', charset='utf8')
cur = conn.cursor()

#cur.execute("UPDATE sampk SET row02='4', row03='4' WHERE row01=3")
cur.execute(sql)

conn.commit()
conn.close()