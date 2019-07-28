def bulk(self):
    print("%s is yelling..." %self.name)

class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating %s..." %(self.name,food))


# d = Dog("Henry")
# choice = input("＞＞：").strip()
# getattr(d,choice)("ss")
#
# name = ['alex','jack']
# data = {}
#names[3]
try:
    a = 1
    print(a)
    #name[3]
    # data['name']
    # open("tes.txt")
except (KeyError,IndexError) as e:
    print("沒有這個key,",e)
except IndexError as e:
    print("列表操作失誤",e)
except Exception as e:
    print("未知錯誤",e)
else:
    print("一切正常 ")
finally:
    print("不管有沒有錯,都執行")
#except IndexError as e:
   # print("列表操作失誤",e)
