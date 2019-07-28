name = "my name is henry"

print(name.capitalize()) #字首變大寫
print(name.center(30,"-")) #字置中 左右增加'-' 30 = 字 + -
print(name.endswith("ry")) #判斷字符串的結尾
print(name.expandtabs(tabsize = 30))
print(name.find("my"))
print(name[name.find("my"):9]) #切片

name2 = "My name {name} and i am {year} old."
print(name2.format_map({'name':'Henry' , 'year':18} ))
print('ab123'.isalnum()) #只能英文跟數字
print('ab'.isalpha()) # 只能英文字符
print('123132132123'.isdecimal()) #是否只包含十进制字符
print(['+' .join(['1','2','3','4'])])
print('kkkkkk'.upper())

p = str.maketrans("abcdef","123456") #a=1 b=2 ...
print('alex li'.translate(p))

print('Zhang wei fu ck kkkk'.split(' '))