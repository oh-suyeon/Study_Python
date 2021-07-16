from flask import Flask, session, render_template, request, jsonify, escape
import requests
import json

# 출처 https://github.com/dpwls64/KAKAO-API

app = Flask(__name__,
            static_url_path='',
            static_folder='static'
            )


@app.route("/")
@app.route("/kakaopay")
def main():
    return render_template('main.html')


@app.route("/kakaopay/paymethod.ajax", methods=['POST']) # 결제 준비 ([pay] 버튼 클릭 시)
def paymethod():
    if request.method == 'POST':
        
        postdata = request.get_json(force=True)
        print(postdata['item_name'])
        print(postdata['qantity'])
        print(postdata['total_amount'])
        
        URL = 'https://kapi.kakao.com/v1/payment/ready' #결제 준비 API 호출
        headers = {
            'Authorization': "KakaoAK " + "d13a6511a060fb5b95c04824aa9c981d", #APP_ADMIN_KEY
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
        }
        params = {
            "cid": "TC0ONETIME",            #가맹점 코드 (test)
            "partner_order_id": "1001",     #가맹점 주문번호
            "partner_user_id": "testuser",  #가맹점 회원 id
            "item_name": postdata['item_name'],          #상품명
            "quantity": postdata['qantity'],             #상품 수량 
            "total_amount": postdata['total_amount'],    #상품 총액          
            "tax_free_amount": 0,           #상품 비과세 금액  
            # "vat_amount" : 200,             #상품 부가세 금액 (값을 보내지 않을 경우 자동 계산) - ajax로 값을 보낼 거니까 자동 계산하게 둠
            "approval_url": "http://127.0.0.1:5000/kakaopay/success",   #결제 성공 시 redirect url - pg_token가 쿼리로 함께 감
            "cancel_url": "http://127.0.0.1:5000/kakaopay/cancel",      #결제 취소 시 redirect url 
            "fail_url": "http://127.0.0.1:5000/kakaopay/fail"           #결제 실패 시 redirect url
        }
        
        res = requests.post(URL, headers=headers, params=params) # 결제 정보를 서버에 전달하고 응답 받아 res에 저장
        app.tib = res.json()['tid']  # res에 담긴 tid(결제 고유 번호)를 세션(??)에 저장

        return jsonify({'next_url': res.json()['next_redirect_pc_url']}) # res에 담긴 next_redirect_pc_url(사용자 정보 입력 화면 Redirect URL)를 반환

    # return render_template('main.html') # 왜 있는 걸까? 없어도 정상 작동되는데



@app.route("/kakaopay/success", methods=['POST', 'GET']) # 결제 승인
def sucess():
    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "d13a6511a060fb5b95c04824aa9c981d",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    params = {
        "cid": "TC0ONETIME",  # 테스트용 가맹점 코드
        "tid": app.tib,  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": "1001",  # 주문번호. 결제 준비 API 요청과 일치해야 함
        "partner_user_id": "testuser",  # 유저 아이디. 결제 준비 API 요청과 일치해야 함
        "pg_token": request.args.get("pg_token")  # approval_url(/kakaopay/success)으로 리다이렉션했을 때 쿼리 스트링으로 받은(GET) pg토큰. 결제승인 요청을 인증하는 토큰.
    }

    res = requests.post(URL, headers=headers, params=params)
    amount = res.json()['amount']['total'] # 결제 금액 (전체 결제 금액)
    res = res.json() # 결제 승인 시각, 가맹점 주문번호, 상품 이름 등의 정보 들어있음
    context = {
        'res': res, 
        'amount': amount 
    }
    return render_template('success.html', context=context, res=res)


@app.route("/kakaopay/cancel", methods=['POST', 'GET']) # 결제 대기 중 결제 취소. 결제 준비 화면(/kakaopay/paymethod.ajax)에서 [X]버튼 클릭했을 경우.  
def cancel():                                           # 결제 고유번호인 tid에 해당하는 결제건에 대해 지정한 금액만큼 결제 취소를 요청
    URL = "https://kapi.kakao.com/v1/payment/order"
    headers = {
        "Authorization": "KakaoAK " + "d13a6511a060fb5b95c04824aa9c981d",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    params = {
        "cid": "TC0ONETIME",  # 가맹점 코드
        "tid": app.tib  # 결제 고유 코드
    }

    res = requests.post(URL, headers=headers, params=params) #성공 시 응답은 바디에 JSON 객체로 결제 취소 내역을 포함
    amount = res.json()['cancel_available_amount']['total'] #취소 가능 금액 중 전체 취소 가능 금액

    context = {
        'res': res,
        'cancel_available_amount': amount
    }
    
    if res.json()['status'] == "QUIT_PAYMENT": #사용자가 결제 중단
        res = res.json()
        return render_template('cancel.html', params=params, res=res, context=context)


@app.route("/kakaopay/fail", methods=['POST', 'GET']) # 테스트 결제에선 결제 실패를 시연할 수 없음
def fail():
    return render_template('fail.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host='127.0.0.1', port=5000, debug=True)