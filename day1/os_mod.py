#OS 模組基本用法
import os

cmd_res1 = os.system("dir") #執行命令 不保存結果
cmd_res2 = os.popen("dir").read()
os.mkdir("day2") #在當前目錄新增一資料夾
print("-->", cmd_res2 )