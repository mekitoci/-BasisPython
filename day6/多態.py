class Animal(object):
    def __init__(self,name):
        self.name = name

    def talk(self):
        pass

    @staticmethod
    def animal_talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print("Meow!")


class Dog(Animal):
    def talk(self):
        print("Woof! Woof!")

def animal_talk(obj):
    obj.talk()

d = Dog("謝尚衛")
#print(d.talk())

c = Cat("余幸芳")
#print(c.talk())

Animal.animal_talk(c)
Animal.animal_talk(d)
