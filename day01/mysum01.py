# 1~20 중 짝수 합 구하기
# 맞는지 검증해보려면 range(1, 5)로 해서 맞나 본다.

sum = 0

for i in range(1, 21) :
    if not i%2 : 
        sum+=i
        
print("sum",sum) 


