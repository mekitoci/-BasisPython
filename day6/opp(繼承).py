#class People: #經典類
class People(object): #新式類

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []

    def eat(self)   :
        print("%s is eating..." %(self.name))

    def sleep(self):
        print("%s is sleeping..." %(self.name))

    def talk(self):
        print("%s is talking..." %(self.name))

class Relation(object):

    def make_friends(self,obj):
        print("%s is making friends with %s" %(self.name,obj.name))
        self.friends.append(obj)

class Man(People,Relation):
    def __init__(self,name,age,money):
        #People.__init__(self,name,age)
        super(Man,self).__init__(name,age) #新式類的寫法
        self.money = money
        print("%s 一出生就有%s元money" %(self.name,self.money))

    def piao(self):
        print("%s is piaoing ..... 20s .. done." %self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping...")

class Woman(People,Relation):

    def get_birth(self):
        print("%s is born a baby..." % self.name)

m1 = Man("Henry",18 ,10)
# m1.eat()
# m1.piao()
# m1.sleep()

w1 = Woman("Kathy",17)
# w1.get_birth()

m1.make_friends(w1)
print(m1.friends[0].name)