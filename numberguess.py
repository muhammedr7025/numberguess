import random
print("GUESS THE NUMBER \n")
rand=random.randrange(1,50)
a=0
c=5
while a<c:
    num=int(input("Guess a number between 1&50: "))
    a=a+1
    if rand==num:
        print("you have won!")
    else:
        print("try again")
