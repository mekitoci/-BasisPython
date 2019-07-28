#遞迴
#1.明確的結束條件
#2.問題規模每遞迴一次都應該比上一次的問題規模有所減少
#3.效率低

def calc(n):
    print(n)
    if int(n/2) >0:
        return calc(int(n / 2))

calc(10)
