from flask import Flask, request, jsonify
import json
from flask.templating import render_template
app = Flask(__name__, static_url_path="", static_folder="static")

@app.route('/') 
@app.route('/index')
def hello():
    return render_template(
            'index.html',
        )

@app.route('/ajax', methods=['POST'])
def ajax():
    
    #json 데이터를 파이썬 데이터 형식으로 변환해 가져오기
    data = request.get_json()
    print(data)
    
    #json 데이터를 내보내는 flask의 함수. json.dumps()로 대체 가능함.
    return jsonify(result = "success", result2= data)

if __name__=='__main__':
    app.run(debug=True) 

