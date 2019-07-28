
class Dog(object):
    #n = 333
    name = "Kathy"
    def __init__(self,name):
        self.name = name

    @classmethod
    def eat(self,food): #只能調用類變量
        print("%s is eating %s" %(self.name,food))

    def talk(self):
        print("%s  is talking" %self.name)

d = Dog("Henry")
d.eat("11")