def add(a,b):
    return a + b


def sub(a,b):
    return a - b


def mult(a,b):
    return a * b



def div(a,b):
    return a / b

print("select the operation")
print("1.addition")
print("2.substraction")
print("3.multipliction")
print("4.division")

ch= input("select option :")
a = int(input("enter first value : "))
b = int(input("enter second value : "))

if ch == "1":
    print(a," + ",b," = ",add(a,b))

elif ch == "2":
    print(a," - ",b," = ",sub(a,b))
elif ch == "3":
    print(a," * ",b," = ",mult(a,b))
elif ch == "4":
    print(a," / ",b," = ",div(a,b))
else:
    print("error:invalid choice user.")


