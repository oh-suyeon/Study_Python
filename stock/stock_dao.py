import pymysql

class StockDao:
    
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='_stock_old', charset='utf8')
        self.cur = self.conn.cursor()
        
    def get_names(self):
        name_list = []
        sql = f"""
            SELECT COLUMN_NAME 
            FROM information_schema.columns 
            WHERE TABLE_NAME = 'stock_sync_0121' 
                AND COLUMN_NAME != 'in_time'
            ORDER BY ordinal_position;
        """
        self.cur.execute(sql)
        rows= self.cur.fetchall()
        for row in rows :
            name_list.append(row[0])
        return name_list
    
    def get_price(self, s_name) :
        price_list = []
        sql = f"""
            SELECT {s_name}
            FROM stock_sync_0121
            ORDER BY in_time;
        """
        self.cur.execute(sql)
        rows= self.cur.fetchall()
        for row in rows :
            price_list.append(row[0])
        return price_list
        
    def count_days(self):
        cnt = 0;
        sql = f"""
            SELECT COUNT(in_time) AS cnt
            FROM stock_sync_0121
        """
        self.cur.execute(sql)
        cnt = self.cur.fetchall()
        cnt = cnt[0][0]
        return cnt

    def __del__(self):
        self.cur.close() 
        self.conn.close() 
    

if __name__=='__main__' :
    sd = StockDao()
    cnt = sd.count_days()
    print(cnt)
