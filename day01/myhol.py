from random import random

mine = input("홀/짝을 고르세요")
com = ""
result = ""

print(mine)

rnd = random()
if rnd > 0.5 :
    com = "홀"
else :
    com = "짝"

if mine==com :
    result = "승리"
else :
    result = "패배"

print("mine:", mine)
print("com:", com)
print("result:", result)