def match_words(words):
    count = 0
    list = []
    for i in words:
        if (len(i) > 1 and i[0] == i[-1]):
            count = count + 1
            list.append(i)
    print(list)
    return count

temp = match_words(['aba', 'fizz', '1231', 'mym', 'jmg'])
print("Count =",temp)
    

        