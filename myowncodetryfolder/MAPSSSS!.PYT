num1 = [3,4,5,6]
num2 = [1,8,3,6]
result = map(lambda x, y : x+y, num1,num2)
print(list(result))
nums = [2,4,5,6,6,7,8,]

def sq(n):
    return n*n
result = map(sq,nums)
print(list(result))
