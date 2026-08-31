try:
    num = int(input("enter value : "))
    print(num)
except ValueError as e:
    print("Exception : ",e)