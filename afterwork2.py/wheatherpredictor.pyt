wheather = (1,0,0,0,1,1,0)
sunny = 0
rainy = 0

for i in wheather:
    if wheather[i ==0]:
        rainy = rainy +1
    else:
        sunny = sunny +1



if sunny > rainy:
    print("good wheather outside😎")
else:
    print("bad wheather outside😢")