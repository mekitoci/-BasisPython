
class Dog(object):
    """ 這個類是描述狗這個對象的  """
    def __init__(self,name):
        self.name = name
        self.__food = None

    @property #@attribute
    def eat(self): #只能調用類變量
        print("%s is eating %s" %(self.name,self.__food))
    @eat.setter
    def eat(self,food):
        print("set to food:",food)
        self.__food = food
    @eat.deleter
    def eat(self):
        del self.__food
        print("吃完了")

    def talk(self):
        print("%s  is talking" %self.name)

    def __call__(self, *args, **kwargs):
        print("running call" ,args ,kwargs)

    def __str__(self):
        return "<obj:%s>" %self.name


# d(1,2,3,name='henry')
# d.eat
# d.eat = "hamburger"
# d.eat
#
# del d.eat

print(Dog.__dict__) #打印類裡的所有屬性 不包括實例屬性
d = Dog("Henry")
print(d)
print(d.__dict__) #打印所有實例屬性,不包括類屬性