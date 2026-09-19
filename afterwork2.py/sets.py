my_set = {1,2,3}
print(my_set)

my_set = {1.0 ,"hello",(1,2,3,4)}
print(my_set)

my_set = {1,2,3,4,3,2,4}
print(my_set)

my_set = set([1,2,3,2])
print(my_set)

num_set = set([0,1,3,4,5])

print("original set : ",num_set)
num_set.pop()
print("After poping the first element : ")
print(num_set)