
class Dog(object):
    def __init__(self,name):
        self.name = name

    @staticmethod #實際上跟類沒什麼關係了 名義上歸類管
    def eat(self,food): #工具包 form Dog import eat
        print("%s is eating %s" %(self.name,food))

    def talk(self):
        print("%s  is talking" %self.name)

d = Dog("Henry")
d.eat(d,"Hamburger")