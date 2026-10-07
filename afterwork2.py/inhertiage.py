class vehiecle:
    def __init__(self,name,mileage,max_speed):
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed
    
class bus(vehiecle):
    pass
ob = bus("lamborgini", 10, 1000)

print("name : ",ob.name)
print("mileage : ",ob.mileage)
print("max speed : ",ob.max_speed)