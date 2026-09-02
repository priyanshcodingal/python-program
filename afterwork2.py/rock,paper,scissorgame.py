import random

choice = ["rock", "paper",  "scissor"]
computer = random.choice(choice)

user_choice = input("enter a choice from:rock, paper, scissor : ").lower()
print("computer choice : ",computer)

if user_choice == computer:
    print("its a tie -_-")
elif user_choice == "rock" and computer == "scissor":
    print("YOU WINN🎉")
elif user_choice == "scissor" and computer == "paper":
    print("YOU WINN🎉")
elif user_choice == "paper" and computer == "rock":
    print("YOU WINN🎉")
else:
    print("YOU LOOSE😢😢😢")
   