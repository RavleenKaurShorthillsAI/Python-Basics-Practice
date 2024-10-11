m1= int(input("Enter Marks 1: "))
m2= int(input("Enter Marks 2: "))
m3= int(input("Enter Marks 3: "))

total_percentage = 100*((m1 + m2 + m3))/300
if(total_percentage >=40 and m1>=33 and m2>=33 and m3>=33):
    print("You are passed!","Your total percentage is: ",int(total_percentage),"%")
else:
    print("You failed!", "Your Total Percentage is", int(total_percentage),"%")