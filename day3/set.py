#集合


list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)

print(list_1)

list_2 = set([2,6,0,66,22,8,4])
print(list_1,list_2)

#交集
print(list_1.intersection(list_2))
print(list_1 & list_2)

#聯集
print(list_1.union(list_2))
print(list_1 | list_2)

#差集 in list_1 but not in list_2
print(list_1.difference(list_2))
print(list_1 - list_2) # in list1 but not in list2

#子集
list_3 = set([1,3,7])
print(list_3.issubset(list_1)) #list3 is list1 的子集
print(list_1.issuperset(list_3)) #list3是否在list1裡

#對稱差集
print(list_1.symmetric_difference(list_2)) #把交集去掉
print(list_1 ^ list_2)

list_4=set([5,6,8])
print(list_3.isdisjoint(list_4)) #True list_3 and list_4 完全沒交集


#集合沒有插入只有添加
list_1.add(999) #添加一項

list_1.update([5,6,9,8,8,8,77,10]) #添加多項

#刪除
list_1.remove(999)
print(list_1)