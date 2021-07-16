def printNumber():
    for i in range(55000):
        print(i,end="")
        if i % 100 == 0 :
            print()
            
def printChar():
    for i in range(55000):
        print(chr(i),end="")
        if i % 100 == 0 :
            print()

if __name__ == '__main__':
    printNumber()
    printChar()