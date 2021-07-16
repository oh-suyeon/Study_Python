#Python Thread 예제1
import threading
 
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
    my_t1 = threading.Thread(target=printNumber)
    my_t2 = threading.Thread(target=printChar)
    my_t1.start()
    my_t2.start()
