print("김소희")
print("이여강")
print("백지혜")

arr = ["김소희", "이여강", "백지혜"];

# 배열에 있는 것 하나 하나 꺼낸다 
for item in arr:
    print(item)

print()

# 그래서 인덱스를 추가해봐도 불편하다
idx = 0
for item in arr:
    print(idx,item)
    idx+=1

print()
    
# 그래서 enumerate 함수를 쓴다
for idx,item in enumerate(arr):
    print(idx,item)

