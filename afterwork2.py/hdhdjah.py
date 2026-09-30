import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

all_characters = lower + upper + numbers

password = ""

for i in range(8):
    password = password + random.choice(all_characters)

print("Your password is:", password)