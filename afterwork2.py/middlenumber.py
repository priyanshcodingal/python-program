num=int(input("enter a number:"))
t = num
numlen = 0

while t > 0:
    numlen=numlen + 1
    t =int(t/10)

if numlen>=4:
    num =int(numlen/2)
    chk = 0
    while num > 0:
        rem = num %10
        if chk ==numlen:
            midone = rem
        elif chk == (numlen - 1):
            midtwo = rem
        num = int(num / 10)
        chk =chk + 1
    product = midone *  midtwo

    
    print("product of", midone, "and", midtwo, "is", product)
else:
    print("number is less than 4 digits")

    