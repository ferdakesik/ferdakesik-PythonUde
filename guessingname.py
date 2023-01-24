import random

highest=10
answer=random.randint(1,highest)
print(answer )

print("print guess numbrt between 1 and {}: ".format(highest))
guess= int(input())

if guess==answer:
    print("you got it first time")
else:
    if guess < answer:
        print("please guess higher")
    else:
        print("please guess lower")
    guess=int(input())
    if guess==answer:
        print("well done , you guessed it")
    else:
        print("sorry,you have not guessed correctly")