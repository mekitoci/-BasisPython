#args 存成tuple的形式
"""
def test1(*args): #args 參照組 在函数定义中使用*args和**kwargs传递可变长参数
    print(args)

test1(1,23,4,5,6,7,8,9)
"""

"""
#**kwags 把N個關鍵字參數，轉換成字典形式
def test2(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])


test2(name='alex',age=8,sex='F')
test2(**{'name':'alex','age':8,'sex':'F'})
"""

def test3(name,**kwargs):
    print(name)
    print(kwargs)

test3('alex')


