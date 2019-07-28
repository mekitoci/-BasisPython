msg = "我愛金門高中"

print(msg.encode(encoding="utf-8")) #編碼
print(msg.encode(encoding="utf-8").decode()) #解碼

a = msg.encode()

print(type(msg)) #str
print(type(a)) # bytes 二進制
