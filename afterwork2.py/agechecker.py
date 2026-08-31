
try:
    user_input = int(input("enter a your age : "))

    if user_input/2 == 0:
        print("your age is even")
    else:
        print("your age is odd")
except ValueError:
    print("wrong age please try again")
