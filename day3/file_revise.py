import sys
f = open("yesterday","r",encoding="utf-8")
f_new = open("yesterday.bak","w",encoding="utf-8")

find_str = sys.argv[1]
replace_str = sys.argv[2]

for line in f:
    if "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受","肆意的快乐等Henry享受")
    f_new.write(line)

f.close()
f_new.close()
