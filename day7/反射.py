def bulk(self):
    print("%s is yelling..." %self.name)

class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating %s..." %(self.name,food))

d = Dog("Henry")
choice = input("＞＞：").strip()

if hasattr(d,choice):
    delattr(d,choice)
    # attr = getattr(d,choice)
    # # func("Jax")
    # setattr(d,choice,"LeeSin")
else:
    # setattr(d,choice,bulk)
    # d.fuck(d)
    setattr(d,choice,bulk) #d.talk = bulk
    func = getattr(d,choice)
    func(d)


