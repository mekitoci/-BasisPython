lover = "Melody"

def change_name(name):
    global lover
    lover = "LOVE mmmm"
    print("before change",name,lover)
    name = "Kathy" #這個函數就是這個變量的作用域
    print("after change",name)

    name = "Henry"
    change_name(name)
    print(name)
    print(lover)
