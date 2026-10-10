class myclass:
    __privatevar = 1000

    def __privatefucnc(self):
        print("its private function")

    def hello(self):
        print("value of private cariable : ",myclass._privatevar)

ob = myclass()
ob.hello()
ob.__privatevar




