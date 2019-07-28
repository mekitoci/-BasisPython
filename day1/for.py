for i in range(3):
    age = int(inpu  t("Guess age:"))
    if age == correct_age:
        print("Yes,you got it!!")
        break
    elif age < correct_age:
        print("Think higher...")
    else:
        print("Think smaller!!")
else:
    print("you have tried too many times.. fuck off!!")
