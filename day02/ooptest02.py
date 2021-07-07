class Dog:
    def __init__(self) :
        self.flag_bark = True
    
    def do_surgery(self):
        self.flag_bark = False
    

class Bird:
    def __init__(self):
        self.skill_fly = 0
    
    def learn(self):
        self.skill_fly += 1


class GaeSae(Dog,Bird):
    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)
        print("생성")
    
    def __str__(self):
        return "{},{}".format(self.flag_bark, self.skill_fly)
    
    def __del__(self):
        print("소멸")


if __name__=="__main__" :
    
    gaeSae = GaeSae()
    print("초기값 : ", gaeSae)
    
    gaeSae.do_surgery()
    print("do_surgery : ", gaeSae)
    
    gaeSae.learn()
    print("learn : ", gaeSae)
    
    
    
    