import random

guess = random.randint(0, 50)


while True:
    user_guess = int(input("enter a guess : "))
    if user_guess == guess:
        print("you are the winner")
    elif user_guess > guess:
        print("hint:think of a lower number")
    else:
        print("think of a higher number")

