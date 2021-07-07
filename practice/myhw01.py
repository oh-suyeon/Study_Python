#가위바위보

from random import random

mine = input("가위, 바위, 보를 입력하세요")
com = ""
result = ""

rnd = random()

if rnd >= 0.33 : 
    com = "가위"
elif rnd >= 0.66 :
    com = "바위"
else :
    com = "보"

if com == mine : 
    result = "비겼습니다"
elif (com=="가위" and mine =="바위") or (com=="바위" and mine =="보") or (com=="보" and mine =="가위") : 
    result = "이겼습니다"
else :
    result = "졌습니다"
    
print("mine : ",mine)
print("com : ",com)
print("result : ",result)