import pymysql

# insert function
## connection(socket) 걸 때가 메모리를 가장 많이 잡아먹는다.
### socket을 한번 열 때 다 insert해야 한다. (루프 돌때마다 열고 닫으면 안된다. ) 

conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='mypydb', charset='utf8')
cur = conn.cursor()

def insertStock(s_code, c_name, price, crw_date) : 
    sql = "insert into stock (s_code, c_name, price, crw_date) values (%s, %s, %s, %s)"
    val = (s_code, c_name, price, crw_date)
    cur. execute(sql, val)
    conn.commit()


insertStock('1', '1', '1', '1')

conn.close()