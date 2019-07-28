def hanoi(n,x,y,z): #zxy yxz
    if n == 1: #1 x-z
        print(x,"----CC>",z,n)
    else:
        hanoi(n-1,x,z,y) #"2 xzy --->  #x=y z=x y=z 1 x=y z=x y=z
        print(x,"----->",z,n) # 2 xzy 3 xyz
        hanoi(n-1,y,x,z) # y=x x=z z=y 2yxz

number = int(input("請輸入河內塔的層數："))
hanoi(number,"x","y","z")