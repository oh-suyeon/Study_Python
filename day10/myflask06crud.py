from flask import Flask,request,jsonify
from flask.templating import render_template
from day10.mydao_emp import DaoEmp

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route('/emp')
def emp():
    
    de = DaoEmp()
    emp_arr = de.selctlist()
    
    return render_template(
            'emp.html',
            emp_arr = emp_arr
        )

@app.route('/emp_insert.ajax', methods=['POST'])
def ajax():
    d = request.get_json()
    print(d['e_id'])
    
    de = DaoEmp()
    cnt = de.insert(d['e_id'], d['e_name'], d['tel'], d['address'])
    
    msg = "fail"
    if cnt == 1 :
        msg = "success"
    
    return jsonify(result = msg)


if __name__=='__main__':
    app.run(debug=True) 

