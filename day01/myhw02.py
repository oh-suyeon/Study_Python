#첫째 수, 끝 수 입력받아 더하기

first = input("첫째 수를 입력하세요")
last = input("끝 수를 입력하세요")

sum = 0;

for i in range(int(first), int(last)+1) :
    sum += i   

print("sum : ",sum)