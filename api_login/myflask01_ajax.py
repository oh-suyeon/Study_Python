from flask import Flask, render_template, request, jsonify

app = Flask(
    __name__
    , static_folder='static'
    , static_url_path='')


@app.route("/")
@app.route("/login")
def index():
    return render_template('login.html')


@app.route('/loginCheck')
def ajax():
    return render_template('loginCheck.html')


@app.route('/naver_login')
def login():
    return render_template('login.html')


@app.route('/callback')
def callback():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)