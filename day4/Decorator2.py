#函數就是變量
def bar():
    print('in the bar')

def foo():
    print('in the foo')
    bar()

calc = lambda x:x*3
foo()