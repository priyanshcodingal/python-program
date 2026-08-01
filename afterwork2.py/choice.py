print("select your ride")
print("1.car")
print("2.bike")
ride = input("enter your choice:")
if ride == "1":
    print("select your car")
    print("1. BMW")
    print("2. Audi")
    car = input("enter your choice:")
    if car == "1":
        print("you have selected BMW")
    elif car == "2":
        print("you have selected Audi")
    else:
        print("invalid choice")
elif ride == "2":
    print("select your bike")
    print("1. Yamaha")
    print("2. Honda")
    bike = input("enter your choice:")  
    if bike == "1":
            print("you have selected Yamaha")
    elif bike == "2":
            print("you have selected Honda")
    else:
            print("invalid choice")
