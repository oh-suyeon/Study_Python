from flask import Flask,request,jsonify
from flask.templating import render_template
from day13.mydao_exam import DaoExam

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route('/')
@app.route('/exam')
def exam():
    
    dex = DaoExam()
    exam_arr = dex.selctlist()
    
    return render_template(
            'exam.html',
            exam_arr = exam_arr
        )


@app.route('/exam_insert.axios', methods=['POST'])
def axios_exam_insert():
    
    d = request.get_json()
    dex = DaoExam()
    cnt = dex.insert(d['e_id'], d['kor'], d['eng'], d['math'])
    
    msg = "fail"
    if cnt == 1 :
        msg = "success"
    
    return jsonify(result = msg)


@app.route('/exam_update.axios', methods=['POST'])
def axios_exam_update():
    
    d = request.get_json()
    dex = DaoExam()
    cnt = dex.update(d['exam_id'], d['e_id'], d['kor'], d['eng'], d['math'])
    
    msg = "fail"
    if cnt == 1 :
        msg = "success"
    
    return jsonify(result = msg)


@app.route('/exam_delete.axios', methods=['POST'])
def axios_exam_delete():
    
    d = request.get_json()
    dex = DaoExam()
    cnt = dex.delete(d['exam_id'])
    
    msg = "fail"
    if cnt == 1 :
        msg = "success"
    
    return jsonify(result = msg)


if __name__=='__main__':
    app.run(debug=True) 

