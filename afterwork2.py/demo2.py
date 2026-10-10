class point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

ob = point(9, 6)
print(ob)
