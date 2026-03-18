try:
    num=int(input("enter a number"))
    if num%2==0:
      print(num)
except SyntaxError as ex:
   print(ex)
except ValueError as ex:
   print(ex)
except ZeroDivisionError as ex:
   print(ex)
   20