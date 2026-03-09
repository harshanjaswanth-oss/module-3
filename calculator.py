def addtion(a,b):
    return a+b

def subraction(a,b):
    return a-b

def multipy(a,b):
    return a*b

def divide(a,b):
    return a/b

print("1  addtion-----2 subraction-----3 multipy-----4 divide")

choice=int(input("enter your choice")) 
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
if choice==1:
    print(addtion(num1,num2))

elif choice==2:
     print(subraction(num2,num2))

elif choice==3:
    print(multipy(num1,num2))

elif choice==4:
    print(divide(num1,num2))

else:
    print("invalid choice")


            