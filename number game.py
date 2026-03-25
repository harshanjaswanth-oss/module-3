import random

num=(random.randint(1,10))

while True:
           guess=int(input("enter a number from one to ten"))
           if num==guess:
                   print("YOU WIN THE GAME")
                   print("The number was",guess)
                   break
           else:
                   print("guess was not correct")
                   print("enter another number")

