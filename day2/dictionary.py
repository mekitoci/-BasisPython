#key - value
info = {
    '510052' : "Kathy",
    '510289' : "Wei",
    '510087' : "Henry",
    '510098' : "Melody"
}

print(info)
info["510052"] = "凱西"

#查找
print(info.get("510073")) #確認字典有無數據
print('510073' in info) # True or False

#del
# del info["510289"]
info.pop("510289")
info.popitem() #隨機刪除
print(info)

for i in info:
    print(i,info[i])

for k,v in info.items():
    print(k,v)

for g in info.values():
    print(g)