class computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("selling price : ",self.__maxprice)
    def setmaxprice(self, price):
        self.__maxprice = price

ob = computer()
ob.sell()


ob.__maxprice = 1000
ob.sell()


ob.setmaxprice(100)
ob.sell()