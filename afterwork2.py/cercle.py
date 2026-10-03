class circle:
    def __init__(self,radius):
        self.radius = radius
    pi = 3.14
    def Areaofceircle(self):
        return 3.14 * self.radius * self.radius
    def parameterccircle(self):
        return 2 * 3.14 * self.radius


ob = circle(13)
print(ob.Areaofceircle())
print(ob.parameterccircle())