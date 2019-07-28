import random

checkcode = ""

for i in range(4):
    current = random.randrange(0,4) #0,1,2,3 if  == i 往下跑
    #字母
    if current == i:
        tmp = chr(random.randint(65,90))
    #數字
    else:
        tmp = random.randint(0,9)

    checkcode += str(tmp)

print(checkcode)