class person:
     def __init__ (self,name,idnum):
        self.name = name
        self.idnum = idnum
     def display(self):
        print("Name :",self.name)
        print("Id number : ",self.idnum)

class employee(person):
    def __init__ (self, name, idnum, salery, post):
        self.salery = salery
        self.post = post


        person.__init__(self, name, idnum )

ob = employee("priyansh", 1001, 10000000000000000000, "ceo")
ob.display()
 
     
     
     