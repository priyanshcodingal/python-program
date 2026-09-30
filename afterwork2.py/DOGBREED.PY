class dog:
    dog_name = "jerry"
    def __init__(self,breed,max_height):
        self.breed = breed
        self.max_height = max_height
ob1 = dog("golden retriver",1.20)
ob2 = dog("puppy",0.56)
print(ob1.breed,"max height is",ob1.max_height)
    