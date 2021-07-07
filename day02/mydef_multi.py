# 리턴을 여러 개할 수 있음
def add_min_mul_div(a,b):
    return a+b,a-b,a*b,a/b

# 하나만 덜 받아도 오류가 남
sum,min,mul,div = add_min_mul_div(2,3)

print(sum)
print(min)
print(mul)
print(div)