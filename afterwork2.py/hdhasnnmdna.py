import random
class fruits:
    def __init__(self):
        self.fruits = {"apple":"red", "strawberry":"pink","watermelon":"green"}

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("whats the color",fruit)
            user_input = input()

            if(user_input.lower() == color):
                print("correct")
            else:
                print("wrong")
            option =  int(input("enter 0 if you want to continue or enter 1 if you wnat to end"))
            if(option):
                break
ob = fruits()
ob.quiz()

