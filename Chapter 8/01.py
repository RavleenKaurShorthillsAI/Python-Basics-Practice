def greatest(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print(f"Greatest number is: {num1}")
    elif(num2>num1 and num2>num3):
        print(f"Greatest number is: {num2}")
    elif(num3>num1 and num3>num2):
        print(f"Greatest number is: {num2}")


num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))

greatest(num1,num2,num3)