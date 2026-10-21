class A:
    def __init__(self,a):
        self.a = a

    def __lt__(self, other):
        if (self.a < other.a):
            return "ob1 is less then ob2"
        else:
            return "ob2 is less then ob1"

    def __eq__(self,other):
        if(self.a == other.a):
            return "both are equal"
        else:
            return "They are diffrent"

ob1 = A(2)    
ob2 = A(3)
print(ob1 < ob2)