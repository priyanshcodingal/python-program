test_dict = {"codingal":2, "is":2, "best":2, "for":2, "coding":1}

print("original Dictionary : "+str(test_dict))

k = 2

count = 0
for key in test_dict:
    if test_dict[key]==k:
        count =count +1

print("Frequency of ",k," is ",count)