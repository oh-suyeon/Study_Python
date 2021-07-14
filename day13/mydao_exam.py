import pymysql

class DaoExam:
    
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='mypydb', charset='utf8')
        self.cur = self.conn.cursor()
        
    def insert(self, e_id, kor, eng, math):
        sql = f"""
            INSERT INTO exam 
                (e_id
                , kor
                , eng
                , math
                , in_user_id
                , in_date 
                , up_user_id
                , up_date) 
            VALUES 
                ( '{e_id}'
                , '{kor}'
                , '{eng}'
                , '{math}'
                , '1'
                , DATE_FORMAT(NOW(), '%Y%m%d.%H%m%s')
                , '1'
                , DATE_FORMAT(NOW(), '%Y%m%d.%H%m%s'))
            """
        self.cur.execute(sql)
        self.conn.commit()
        cnt = self.cur.rowcount
        return cnt
    
    def update(self, exam_id, e_id, kor, eng, math):
        sql = f"""
            UPDATE exam 
            SET e_id         = '{e_id}'
                , kor        = '{kor}'
                , eng        = '{eng}' 
                , math       = '{math}'
                , up_user_id = '1'
                , up_date    = DATE_FORMAT(NOW(), '%Y%m%d.%H%m%s')
            WHERE exam_id = {exam_id} 
            """
        self.cur.execute(sql)
        self.conn.commit()
        cnt = self.cur.rowcount
        return cnt
    
    def delete(self, exam_id):    
        sql = f"""
            DELETE FROM exam
            WHERE exam_id = '{exam_id}'
            """
        self.cur.execute(sql)
        self.conn.commit()
        cnt = self.cur.rowcount
        return cnt
        
    def selctlist(self): 
        ret = []
        sql = """ 
            select 
                exam_id
                ,e_id
                ,kor
                ,eng
                ,math
                ,in_user_id
                ,in_date
                ,up_user_id
                ,up_date
            from exam
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for row in rows:
            ret.append({'exam_id':row[0],'e_id':row[1],'kor':row[2],'eng':row[3],'math':row[4],'in_user_id':row[5],'in_date':row[6],'up_user_id':row[7],'up_date':row[8]}); 
        return ret
    
    def __del__(self):
        self.cur.close()
        self.conn.close()

if __name__=='__main__' :
    dex = DaoExam()
    list = dex.selctlist()
    print(list)
