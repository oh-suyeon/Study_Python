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
    data = request.get_json()
    print(data)
    return jsonify(result = "success", result2= data)

if __name__=='__main__':
    app.run(debug=True) 

