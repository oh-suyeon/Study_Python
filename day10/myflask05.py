from flask import Flask
import json
from flask.templating import render_template
app = Flask(__name__)

@app.route('/') 
@app.route('/emp') # 이렇게 하면 emp 붙였을 때도 나온다.
def hello():
    
    arr = ["김소희", "이여강", "오수연", "최윤지", "김지수"]
    
    arr2 = [
            {'name':'김소희','tel':'010-2222-3333'},
            {'name':'이여강','tel':'010-3333-4444'}
        ]
    
    return render_template(
            'myflask05.html',
            my_str = "Hello World!!22",
            arr = arr,
            arr2 = arr2
        )

if __name__=='__main__':
    app.run() 

