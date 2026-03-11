def cube(num):
    cube=num*num*num
    print("cube",cube)

def divisible (num):
     
     if num%3==0:
      cube(num) 
     else:
        print("not divisible by 3")
num=int(input("enter the value of num"))
divisible(num)
