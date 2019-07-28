#while 迴圈 ★ while-else 用法+ for-else

correct_age = 18
count = 0

while count < 3:
    age = int(input("Guess age:"))
    if age == correct_age:
        print("Yes,you got it!!")
        break
    elif age < correct_age:
        print("Think higher...")
    else:
        print("Think smaller!!")
    count += 1

    if count == 3:
        countine_confirm = input("Do you want to keep guessing..?")
        if countine_confirm != "n":
            count = 0
else:
    print("you have tried too many times.. fuck off!!")






