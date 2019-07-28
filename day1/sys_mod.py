import sys
import time
#print(sys.path) #打印環境變量
#print(sys.argv)

for i in range(50):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.5)