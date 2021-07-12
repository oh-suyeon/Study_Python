import pymysql

class DaoEmp:
    
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='mypydb', charset='utf8')
        self.cur = self.conn.cursor()
        
    def insert(self, e_id, e_name, tel, address):
        sql = f"""
            INSERT INTO emp 
                (e_name, tel, address, in_user_id, in_date, up_user_id, up_date) 
            VALUES 
                ('{e_name}', '{tel}', '{address}', '1', DATE_FORMAT(NOW(), '%Y%m%d.%H%m%s'), '1', DATE_FORMAT(NOW(), '%Y%m%d.%H%m%s'))
            """
        self.cur.execute(sql)
        self.conn.commit()
        cnt = self.cur.rowcount
        return cnt
        
    def selctlist(self): 
        ret = []
        sql = """ 
            select 
                e_id
                ,e_name
                ,tel
                ,address
                ,in_user_id
                ,in_date
                ,up_user_id
                ,up_date
            from emp
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for row in rows:
            ret.append({'e_id':row[0],'e_name':row[1],'tel':row[2],'address':row[3],'in_user_id':row[4],'in_date':row[5],'up_user_id':row[6],'up_date':row[7]}); 
        return ret
    
    def __del__(self):
        self.cur.close()
        self.conn.close()

if __name__=='__main__' :
    de = DaoEmp()
    cnt = de.insert('3', '3', '3', '3')
    print(cnt)
