i = False
while not i:
    try:
        n = int(input("enter a number : "))
        while n % 2 == 0:
            print("BYE-_-")
            I = True
    except ValueError:
            print("Invalid value")