import requests
from bs4 import BeautifulSoup
from datetime import datetime
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


url = 'https://vip.mk.co.kr/newSt/rate/item_all.php'

response = requests.get(url)

#response에서 encoding 해도 된다. 
#response.encoding = 'euc-kr'
#html = response.text

html = response.content # not response.text

soup = BeautifulSoup(html.decode('euc-kr', 'replace'), 'html.parser')

tds = soup.select('td .st2')

crw_date = datetime.today().strftime("%Y%m%d.%H%M")

for td in tds :
    
    s_code = td.select_one('a')['title']
    c_name = td.text
    price = td.find_next_sibling().text
    # 부모 태그 찾아서 구할 수 있다. 
    # td.parent.select('td')[1]
    
    # price = price.replace(',', '')
    print("s_code",s_code)
    print("c_name",c_name)
    print("price",price)
    
    #sql = "INSERT INTO stock (s_code, c_name, price, crw_date) VALUES " + "('{}', '{}', '{}', '{}')".format(s_code, c_name, price, crw_date)
    #cur.execute(sql)
    insertStock(s_code, c_name, price, crw_date)
    
conn.close()


