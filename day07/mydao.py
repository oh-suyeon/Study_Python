import pymysql


class DaoStock:
    
    def __init__(self): 
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='mypydb', charset='utf8')
        self.cur = self.conn.cursor()
        
    def get_prices(self, c_name): 
        ret = []
        self.cur.execute(f"""SELECT s_code, c_name, price, crw_date FROM stock WHERE c_name = '{c_name}'""") #최신버전에서 가능
        rows = self.cur.fetchall()
        for row in rows :
            ret.append(row[2])
        return ret
    
    def get_names(self):
        ret = []
        self.cur.execute("SELECT c_name FROM stock GROUP BY c_name")
        rows = self.cur.fetchall()
        for row in rows :
            ret.append(row[0])
        return ret
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
        
if __name__ == '__main__' :
    ds = DaoStock()
    list = ds.get_names()
    print(list)
        
        
        
        