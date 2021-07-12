from flask import Flask,request,jsonify
from flask.templating import render_template
from day10.mydao_emp import DaoEmp

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route('/')
@app.route('/emp')
def emp():
    
    de = DaoEmp()
    emp_arr = de.selctlist()
    
    return render_template(
            'emp.html',
            emp_arr = emp_arr
        )


@app.route('/emp_insert.axios', methods=['POST'])
def emp_insert():
    
    d = request.get_json()
    de = DaoEmp()
    cnt = de.insert(d['e_name'], d['tel'], d['address'])
    
    msg = "fail"
    if cnt == 1 :
        msg = "success"
    
    return jsonify(result = msg)


@app.route('/emp_update.axios', methods=['POST'])
def emp_update():
    
    d = request.get_json()
    de = DaoEmp()
    cnt = de.update(d['e_id'], d['e_name'], d['tel'], d['address'])
    
    msg = "fail"
    if cnt == 1 :
        msg = "success"
    
    return jsonify(result = msg)


@app.route('/emp_delete.axios', methods=['POST'])
def emp_delete():
    
    d = request.get_json()
    de = DaoEmp()
    cnt = de.delete(d['e_id'])
    
    msg = "fail"
    if cnt == 1 :
        msg = "success"
    
    return jsonify(result = msg)


if __name__=='__main__':
    app.run(debug=True) 

