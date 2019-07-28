import copy
names = ["Henry","Peter","Kevin",["Yang","Chen"],"John","Johnny","Brain","Curry"]


#names2 = names.copy() #names 的子集也被改成大寫
names2 = copy.deepcopy(names)

names[2] = "凱文"
names[3][0] = "YANGFAT"
print(names)
print(names2)#透過deepcopy完全獨立 單用copy會有淺copy問題



names.append("Dee") #增加至最後面
names.insert(1,"Curry") #在1前面新增Curry
names[2] = "Klay" #直接更改name[2]的值

#delete method
names.remove("John")
del names[3]
names.pop() # ( )不賦值就刪最後一個
names.pop(4) #刪除第四個
#############
print(names)
print(names[0:5:2]) #切片
print(names[-1]) #取最後一個
print("-----------------------------------")
###############################
print(names.index("Curry")) #index 索引 找字所在位置
print(names[names.index("Curry")]) #從索引值抓取直接打印
print(names.count("Curry")) #計數
#names.clear() 清除列表
#names.reverse() #翻轉列表
#names.sort() #按照ASCII 排列 {特殊符號 ---> 數字 ---> 大寫 ---> 小寫}
names2 = [1,2,3,4]
names.extend(names2)
print(names)

'''