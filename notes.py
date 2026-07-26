amount=int(input("enter the amount"))

note_100=amount//100
note_50=(amount%100)//50
note_10=((amount%100)%50)//10
print("number of 100 rupees note is:",note_100)
print("number of 50 rupees note is:",note_50)
print("number of 10 rupees note is:",note_10)