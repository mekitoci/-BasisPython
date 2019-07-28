class MyType(type):

    def __init__(self,*args,**kwargs):
        print("Mytype __init__",*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ",obj,*args, **kwargs)
        print(self)
        self.__init__(obj,*args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs): #通過new來實例化 先觸發new在觸發init
        print("Mytype __new__",*args,**kwargs)
        return type.__new__(cls, *args, **kwargs)

class Foo(object):
    #__metaclass__ =MyType
    def __init__(self,name):
        self.name = name
        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__",cls)
        return object.__new__(cls) #繼承父親的new方法

# 第一階段 ： 解釋器從上到下執行代碼創建Foo類
# 第二階段 ：通過Foo類創建obj對象
f = Foo("Alex")
print(obj.name)
