def fib(max):
    n , a , b = 0 ,0 ,1
    while n < max:
        #print(b)
        yield b
        a, b = b ,a+b
        n = n+1
    return 'done'

# fib_gen = fib(10)
# print(fib_gen.__next__())

g = fib(6)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print("Generator return value :",e.value)
        break

