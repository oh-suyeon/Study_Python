from flask import Flask, render_template, jsonify, request
import smtplib
from email.mime.text import MIMEText

app=Flask(__name__,  static_url_path="", static_folder='./static/')

gmail_id = ""
naver_id = ""
mailpass = ""

login_info = []
a = open("Info.txt", 'r')
while True:
    line = a.readline()
    if not line:
        break
    arr = line.split(":")
    login_info.append(arr[1].replace("\n",""))
    print(arr[1])
gmail_id = login_info[0] 
naver_id = login_info[1]
mailpass = login_info[2]
a.close()

@app.route('/')
@app.route('/mail')
def home():
    return render_template('mailApi.html')

@app.route('/pass_find.ajax', methods=['POST'])
def pass_find():
    myMail = request.get_json()
    mailAddress = myMail['myMail']
    mail1 = mailAddress.split('@')[1]
    mailStr = mail1.split('.')[0]
    print("어디메일?",mailStr)

    #smtpName = ""
    #네이버인지 구글인지
    
    if mailStr.lower() == "gmail" :
        sendEmail = gmail_id
        recvEmail = mailAddress
        password = mailpass
        smtpName = "smtp.gmail.com"
    
    elif mailStr.lower() == "naver" :
        sendEmail = naver_id
        recvEmail = mailAddress
        password = mailpass
        smtpName = "smtp.naver.com"
        
    #smtp 서버 주소
    smtpPort = 587 #smtp 포트 번호

    text = "회원님의 비밀번호는 '123' 입니다."
    msg = MIMEText(text) #MIMEText(text , _charset = "utf8")
    
    msg['Subject'] ="비밀번호 입니다."
    msg['From'] = sendEmail
    msg['To'] = recvEmail
    print(msg.as_string())
    
    s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
    s.starttls() #TLS 보안 처리
    s.login( sendEmail , password ) #로그인
    s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환해야 합니다.
    s.close() #smtp 서버 연결을 종료합니다.
    
    msg = "success"
    return jsonify(result = msg)

if __name__ == '__main__':
    app.run(debug=True)