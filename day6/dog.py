import time
class dog:
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print("%s :wang wang wang!" % self.name)

d1 = dog("Henry")
d2 = dog("yang")
d3 = dog("chenyang1013")

d1.bulk()
time.sleep(1)
d2.bulk()
time.sleep(1)
d3.bulk()