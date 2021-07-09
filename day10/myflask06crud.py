from flask import Flask
from flask.templating import render_template
from day10.mydao_emp import DaoEmp

app = Flask(__name__)

@app.route('/emp')
def emp():
    
    de = DaoEmp()
    emp_arr = de.selctlist()
    
    return render_template(
            'emp.html',
            emp_arr = emp_arr
        )

if __name__=='__main__':
    app.run() 

