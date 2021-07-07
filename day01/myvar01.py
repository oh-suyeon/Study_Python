a = True
b = 5
c = "5"
d = 6.7 

print(a) # True
print(not a) # False
print(not not a) # True
print(a and a) # True
print(a and not a) # False
print(a or not a) # True

print(b+int(c)) # 10
print(str(b)+c) # 55
print(b,c) # 5 5
print("{}{}".format(b,c)) # 55
print("{}-{}".format(b,c)) # 5-5