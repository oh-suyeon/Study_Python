#수 입력받아 구구단 출력하기

num = input("구구단을 선택하세요")
int_num = int(num)


for i in range(1, 10) :
    print(num, '*', i, '=', int(num)*i)


#for문을 돌리지 않아도 됨
#유지보수 힘드니까 안 쓰는 게 좋음
#한눈에 구구단인 걸 알 수 있는 코드가 좋다
print("{}*{}={}".format(int_num,1,int_num*1))
print("{}*{}={}".format(int_num,2,int_num*2))
print("{}*{}={}".format(int_num,3,int_num*3))
print("{}*{}={}".format(int_num,4,int_num*4))
print("{}*{}={}".format(int_num,5,int_num*5))
print("{}*{}={}".format(int_num,6,int_num*6))
print("{}*{}={}".format(int_num,7,int_num*7))
print("{}*{}={}".format(int_num,8,int_num*8))
print("{}*{}={}".format(int_num,9,int_num*9))