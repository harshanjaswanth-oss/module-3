try:
    num1=int(input("enter the first digit"))
    num2=int(input("enter the second digit"))
    num=num1*num2
    print(num)
except ValueError:
    print("The input is not a integer")