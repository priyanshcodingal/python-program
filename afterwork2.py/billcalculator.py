units = int(input("Enter the number of units consumed: "))
if units < 50:
    amount = units * 2.60
    tax = 25
elif units <= 100:
    amount = units *3.25
    tax = 35
elif units <=200:
    amount = units * 5.26
    tax = 45
else:
    amount = units* 8.45
    tax = 75
bill = amount + tax
print("Your total bill is:", bill)