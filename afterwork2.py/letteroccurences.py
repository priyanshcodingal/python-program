word = input("enter a word : ")
letter = input("enter the letter to check occurrences : ")
i=0
count=0
while i < len(word):
    if word[i] == letter:
        count += 1
    i = i + 1

print("the letter", letter, "occurs", count, "times in the word", word)