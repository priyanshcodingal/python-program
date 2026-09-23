list1 = [1,3,4,5]
list2 = ['a','b','c','d']

print(list(zip(list1,list2)))

list3 = [10,20,30,40]
list4 = [100,200,40,70]

for x, y in zip(list3,list4[::-1]):
    print(x,y)

new_dict = {list3:list4 for list3, list4 in zip(list3,list4)}
print(new_dict)
    