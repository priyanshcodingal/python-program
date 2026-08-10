num=int(input("enter a number:"))
binary = ""
while num > 0:
    rem = num % 2
    binary = str(rem) + binary
    num = num // 2
print("binary of your input is :",binary)