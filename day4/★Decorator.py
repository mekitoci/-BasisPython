#裝飾器
# 定義：本質是函數，(裝飾其他函數)就是為其他函數添加附加功能
#原則：1.不能修改被裝飾函數的源代碼
#            2.不能修改被裝飾函數的調用方式

#實現裝飾器知識具備：
#1.函數即"變量"
#2.高階函數
#                a:把一個函數名當作實參傳給另外一個函數(在不修改被裝飾函數源代碼的情況下)
#                b:返回值中包含函數名
#3.嵌套函數
#高階函數 + 嵌套函數 ==》 裝飾器

import time

def timer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the function run time is %s' %(stop_time - start_time))
    return warpper

@timer
def test1():
    time.sleep(3)
    print('in the test1')

test1()