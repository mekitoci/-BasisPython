def pyramind(n,k):
    for i in range(n,k+1):
        for j in range(n,i+1):
            print(j,end=" ")
        print(" ")

def main():
    num_start = int(input("請輸入起始值(小於終止值):"))
    num_end = int(input("請輸入終止值(大於起始值):"))
    pyramind(num_start,num_end)

main()