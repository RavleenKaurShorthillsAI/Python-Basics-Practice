def goodDay(name):
    print("Good Day, ",name)
    
goodDay("Ravleen")


#For storing a function call in a variable,
#we have to return something from the function

def hello(name):
    print("Hello, ",name)
    return name

a = hello("Ravleen") #This will return whatever the return statement has 
print(a)