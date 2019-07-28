#嵌套函數

def foo():
    print("in the foo")
    def bar(): #局部變量 不可運行
        print("in the bar")
    bar()

foo()

