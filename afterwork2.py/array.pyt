import array as arr

num = arr.array('i',[1,4,2,5,2,3,8])
print("Original Values : ",str(num))

print("number of occurence of 2 in given array is : ",str(num.count(2)))
num.reverse()
print("Num reversed Array : ",str(num))