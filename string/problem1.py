number = int(input("Enter a namber: "))
if number %5 ==0 and number %10 ==0 :
    print("0")
elif number %5 ==0 and number %10!=0:
    print("5")
else : 
    print("other")
    