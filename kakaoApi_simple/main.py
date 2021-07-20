import json
from flask import Flask, session, render_template, request, jsonify, escape
import requests


app = Flask(__name__,
            static_url_path='',
            static_folder='static'
            )

@app.route("/")
@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/kakaopay")
def main():
    item_name = request.args.get("item_name")
    qantity = request.args.get("qantity")
    total_amount = request.args.get("total_amount")
    
    return render_template('main.html',
                           item_name=item_name,
                           qantity=qantity,
                           total_amount=total_amount)


@app.route("/kakaopay/paymethod.ajax", methods=['POST']) 
def paymethod():
    if request.method == 'POST':
        
        postdata = request.get_json(force=True)
        
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            'Authorization': "KakaoAK " + "d13a6511a060fb5b95c04824aa9c981d", 
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
        }
        params = {
            "cid": "TC0ONETIME",            
            "partner_order_id": "1001",     
            "partner_user_id": "testuser",  
            "item_name": postdata['item_name'],          
            "quantity": postdata['qantity'],             
            "total_amount": postdata['total_amount'],        
            "tax_free_amount": 0,          
            "approval_url": "http://127.0.0.1:5000/kakaopay/success",  
            "cancel_url": "http://127.0.0.1:5000/kakaopay/cancel",      
            "fail_url": "http://127.0.0.1:5000/kakaopay/fail"           
        }
        
        res = requests.post(URL, headers=headers, params=params) 
        app.tib = res.json()['tid']  

        return jsonify({'next_url': res.json()['next_redirect_pc_url']}) 



@app.route("/kakaopay/success", methods=['POST', 'GET']) 
def sucess():
    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "d13a6511a060fb5b95c04824aa9c981d",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    params = {
        "cid": "TC0ONETIME", 
        "tid": app.tib,  
        "partner_order_id": "1001", 
        "partner_user_id": "testuser",  
        "pg_token": request.args.get("pg_token")  
    }

    res = requests.post(URL, headers=headers, params=params)
    amount = res.json()['amount']['total'] 
    res = res.json()
    context = {
        'res': res, 
        'amount': amount 
    }
    return render_template('success.html', context=context, res=res)


@app.route("/kakaopay/cancel", methods=['POST', 'GET']) 
def cancel():                                           
    URL = "https://kapi.kakao.com/v1/payment/order"
    headers = {
        "Authorization": "KakaoAK " + "d13a6511a060fb5b95c04824aa9c981d",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    params = {
        "cid": "TC0ONETIME",  
        "tid": app.tib  
    }

    res = requests.post(URL, headers=headers, params=params) 
    amount = res.json()['cancel_available_amount']['total'] 

    context = {
        'res': res,
        'cancel_available_amount': amount
    }
    
    if res.json()['status'] == "QUIT_PAYMENT": 
        res = res.json()
        return render_template('cancel.html', 
                               params=params, 
                               res=res, 
                               context=context)


@app.route("/kakaopay/fail", methods=['POST', 'GET']) 
def fail():
    return render_template('fail.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host='127.0.0.1', port=5000, debug=True)