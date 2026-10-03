class IOstring:
    def __init__(self):
        self.str1 = ""

    def getstring(self):
        self.str1 = input("enter a string")
    def StringUpper (self):
        print("String in upper case : ",self.str1.upper())

ob = IOstring()
ob.getstring()
ob.StringUpper()