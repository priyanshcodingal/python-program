Purchase_price=int(input("enter purchase price"))
selling_price=int(input("enter selling price"))
if selling_price>Purchase_price:
    profit=selling_price-Purchase_price
    print("the profit is",profit)
else:
    loss=purchase_price-selling_price
    print("the loss is",loss)
