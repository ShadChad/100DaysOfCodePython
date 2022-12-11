num = int(input("enter"))
if(num<0):
    print("Number is negative")
elif(num>0):
    print("number is positive")
    if(num<=10):
        print("Number is between 10")
    elif(num>10 and num<+20):
        print("num is between 10 and 20")
    else:
        print("Number is greater than 20")
else:
    print("number is zero")