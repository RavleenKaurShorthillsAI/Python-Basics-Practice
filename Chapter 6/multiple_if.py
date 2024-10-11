a = int(input("Enter your age: "))

if(a%2 == 0):
    print("a is even")

if(a>=18):
    print("Y ou are above the age of consent")
    print("Good to Go")
elif(a<=0):
    print("Invalid Age")

else:
    print("You are below the age of consent")


print("End of Program")