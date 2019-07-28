import time
def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("the func run time is %s" %(stop_time - start_time))
    return deco

@timer #--> test1 = timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")

@timer
def test2(name):
    print("test2",name)

test1()
test2("alex")
# def test2():
#     time.sleep(3)
#     print("in the test2")

