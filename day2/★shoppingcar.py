product_list = [
    ("iPhone",19500),
    ("Mac Pro",48000),
    ("Bike",5000),
    ("Apple Watch",13000),
    ("Coffee",155),
    ("C++ Primer Plus",300)
]

shopping_list = []

salary = input("請輸入工資：")

if salary.isdigit():
    salary = int(salary)
    while True:

        for index, item in enumerate(product_list) : #enumerate同时列出数据和数据下标
            #print(product_list.index(item),item)
            print(index,item)
        user_choice = input("選擇購入商品>>>:")

        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary: #買得起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary))
                else:
                    print("\033[41;1m你的餘額只剩%s啦！\033[0m" %salary)
            else:
                print("此%s號商品不存在！" % user_choice)

        elif user_choice == 'q' :
            print("-------------Shopping List-------------")
            for p in shopping_list:
                print(p)
            print("您的餘額為：%s" % salary)
            exit()

        else:
            print("Invalid option!!")




