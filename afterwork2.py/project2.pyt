tuple1 = (1,2,3,4,5,6)
prod = 1

for i in tuple1:
    prod = prod * tuple1[i-1]
print(prod)
