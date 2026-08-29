def total_Bill_cal(bill_amt, Tip_price):
    total = bill_amt*(1+0.01*Tip_price)
    total = round(total,2)
    print("total bill : ",total)

total_Bill_cal(112, 5)