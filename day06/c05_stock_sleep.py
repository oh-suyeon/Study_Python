import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pymysql
from time import sleep

conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='mypydb', charset='utf8')
cur = conn.cursor()

def insertStock(s_code, c_name, price, crw_date) : 
    sql = "insert into stock (s_code, c_name, price, crw_date) values (%s, %s, %s, %s)"
    val = (s_code, c_name, price, crw_date)
    cur. execute(sql, val)
    conn.commit()


for i in range(6) :  

    crw_date = datetime.today().strftime("%Y%m%d.%H%M")
    
    url = 'https://vip.mk.co.kr/newSt/rate/item_all.php'
    response = requests.get(url)
    html = response.content 
    soup = BeautifulSoup(html.decode('euc-kr', 'replace'), 'html.parser')
    tds = soup.select('td .st2')
    
    for td in tds :
        
        s_code = td.select_one('a')['title']
        c_name = td.text
        price = td.find_next_sibling().text
        price = price.replace(',', '')
        
        insertStock(s_code, c_name, price, crw_date)
            
    sleep(60)  
    

conn.close()


