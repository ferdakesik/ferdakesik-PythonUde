low = 1
high = 1000

print("please think of a number between {} and {}".format(low, high))
input("please enter to start")

guess = 1
while True:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct"
                     .format(guess).casefold())

    if high_low=="h":
        #guess higher. the low end of the range becomes 1 greater than guess.
        low =guess +1
    elif high_low=="l":
        #guess lower. the high end of the range vecomes one less than guess
        high=guess-1
    elif high_low=="c":
        print("i got it in {} guesses".format(guess))
        break
    else:
        print("please enter h,l or c")

    guess = guess+1
