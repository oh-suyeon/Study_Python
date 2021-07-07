class Animal:
    
    def __init__(self): # 생성자는 __init__(self)
        self.age = 0 # 전역 변수를 선언하기. public private 구분하지 않고 다 public
        print("생성자")
        
    def aging(self): # 다 self 붙음
        self.age += 1
    
    def __del__(self):
        print("소멸자")

    
class Human(Animal):
    
    def __init__(self):
        super().__init__() 
        self.skill_speak = 0
        print("생성자")
    
    def learnSpeak(self, step=1):
        self.skill_speak += step

    def __str__(self):
        return "{},{}".format(self.age, self.skill_speak)
    
    def __del__(self):
        super().__del__()


if __name__=="__main__":
    ani = Animal()
    print("Animal:", ani)
    ani.aging()
    print("Animal:", ani)
    
    print()
    
    hum = Human()
    print("Human:", hum)
    hum.aging()
    print("aging->Human:", hum)
    
    print()
    
    print("hum.skill_speak:", hum)
    hum.learnSpeak()
    print("learnSpeak->hum.skill_speak:", hum)

    print()
    
    hum.learnSpeak(5)
    print("learnSpeak(5)->hum.skill_speak:", hum)
    
    