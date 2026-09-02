import random

computer_guess = random.randint(1, 50)


print("welcome to the number guessing game")

while True:
    user_guess = int(input("💖enter a guess between 1 and 50 : "))
    if user_guess == computer_guess:
        print("🎉CONGRATULATIONS!!YOU HAVE GUESSED THE RIGHT NUMBER!!!")
    elif user_guess < computer_guess:
        print("🎉HINT:Think of a higher number;-;")
    else:
        print("🎉HINT:Think of a lower number;-;")
    




