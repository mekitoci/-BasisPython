#類
#調用函數 ---》 執行  ---》返回結果
class Role(object):
    n = 123
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        ##構造函數
        #在實例化時做一些類的初始化的工作
        self.name = name #r1.name = name 實例變量(靜態屬性),作用域就是實例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value #私有函數 無法直接印出
        self.money = money
    def __del__(self): #析構函數
        pass #print("%s 徹底死了。。" %self.name)

    def show_status(self):
        print("name: %s weapon:%s life_value:%s" %(self.name,self.weapon,self.__life_value))

    def shot(self): #類的方法(功能) 動態屬性
        # 開了槍後要減子彈數
        print("shooting...")

    def got_shot(self):
        self.__life_value -= 50
        print("ah...,I got shot...")

    def buy_gun(self,gun_name):
        # 檢查錢夠不夠,買了槍後要扣錢
        print("%s just bought %s" %(self.name,gun_name))


r1 = Role("Alex","police","ak47")# 把一個類變成一個具體對象的過程叫 實例化 (初始化一個類，造了一個對象)
r1.name = "Henry"
r1.n = "改類變量"
print(r1.show_status())
#增加
r1.bullet_prove = True
#刪除
#del r1.weapon

print(r1.n,r1.name,r1.bullet_prove)
r1.got_shot() #Role.got_shot(r1) 調用 self = r1 #調用函數 ---》 執行  ---》返回結果
r1.buy_gun("M4A1")
print(r1.show_status())

r2 = Role("Jack","terrorist","b22") #生成一個角色
print("r2:",r2.n)

r2.n = "ABC"

print(r1.n,r2.n) #r1 改類變量 r2 ABC