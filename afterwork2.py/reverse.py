name = input("enter a string :") 
temp =""


for i in name:
    temp = i + temp
print("original string : ", name)
print("reverse string : ", temp)