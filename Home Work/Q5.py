marks = int(input("enter your marks: "))
if marks>0 and marks<100:
    if marks>=40:
        print("you have passed..")
    elif marks<40:
        print("you have failed..")
else:
    print("its invalid marks")