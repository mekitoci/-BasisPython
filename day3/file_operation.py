#database = open("yesterday",encoding="utf-8").read()
#w = 新建文件 ---> 寫入 #r = 讀取 #a = append 追加
#r+ = 能讀又能寫 #w+ = 能寫又能讀 #rb = 二進制
f = open("yesterday",'w+',encoding="utf-8") #文件句柄 /(句柄)文件的內存資訊
#database = f.read()
#f.write("\n我愛金中,")
#f.write("我要做時代的主人翁")

f.tell() #打印目前位置
f.seek() #回到 X 位置
f.truncate() #清空 /指定數字的話只留指定數字內的字



#high loop 迭代器
'''count = 0
for line in f:
    count = count + 1
    if count == 9:
        print("我是分隔線".center(50,"-"))
        count += 1
        continue
    print(line)
'''
#low loop
'''
for index , line in enumerate(f.readlines()):
    if index == 9:
        print("我是分隔線".center(50,"-"))
        continue
    print(line.strip())
'''
f.close()

