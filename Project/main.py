import random

# 1--> Snake , 2 --> Water, 3 --> Gun

userinput = input("Your Turn: ")
computer = random.choice([1,2,3])
computerDict = {1: "snake", 2: "water", 3: "gun"}
userdict = {"snake": 1, "water":2, "gun":3}
user = userdict[userinput]
print(f"You chose {computerDict[user]}\nComputer chose {computerDict[computer]}")
if(computer == user):
    print("its a Draw!")
else:
    if(computer == 1 and user == 2):
     print("You Lose")
    if(computer == 1 and user == 3):
     print("You Win")
    elif(computer == 2 and user == 1):
     print("You Win")
    elif(computer == 2 and user == 3):
     print("You Lose")
    elif(computer == 3 and user == 2):
     print("You Win")
    elif(computer == 3 and user == 1):
     print("You Lose")
    else:
     print("Something went wrong")