import pymysql

input1 = input("row02 값 입력 > ")
input2 = input("row03 값 입력 > ")

sql = "INSERT INTO sampk (ROW02, ROW03) VALUES " + "('{}', '{}')".format(input1, input2) 

# sql = "insert into sampk (row02, row03) values (%s, %s)" ->https://wikidocs.net/20403
# val = ("3", "3")
# curs. execute(sql, val)

conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='mypydb', charset='utf8')
cur = conn.cursor()

#cur.execute("INSERT INTO sampk (ROW02, ROW03) VALUES ('3', '3')")
cur.execute(sql)

cnt = cur.rowcount

if cnt == 1 :
    print("insert 성공")
else :
    print("insert 실패")

conn.commit()
conn.close()