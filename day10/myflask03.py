from flask import Flask
from flask import request
app = Flask(__name__)

#파라미터 받아 구구단 받기
@app.route("/",methods=['POST']) #기본은 get methods=['POST','GET']
def gugudan():
    dan_str = request.form["dan"] 
    dan = int(dan_str)
    
    gugudan = "{}x{}={}<br />\n".format(dan, 1, dan*1)  
    gugudan += "{}x{}={}<br />\n".format(dan, 2, dan*2) 
    gugudan += "{}x{}={}<br />\n".format(dan, 3, dan*3) 
    gugudan += "{}x{}={}<br />\n".format(dan, 4, dan*4) 
    gugudan += "{}x{}={}<br />\n".format(dan, 5, dan*5) 
    gugudan += "{}x{}={}<br />\n".format(dan, 6, dan*6) 
    gugudan += "{}x{}={}<br />\n".format(dan, 7, dan*7) 
    gugudan += "{}x{}={}<br />\n".format(dan, 8, dan*8) 
    gugudan += "{}x{}={}<br />\n".format(dan, 9, dan*9) 
                
    return gugudan 

if __name__=='__main__':
    app.run() 
