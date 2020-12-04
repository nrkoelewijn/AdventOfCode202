with open('AoC/Day1p1input.txt') as f:
    myList = [line.rstrip('\n') for line in f]
    myList = sorted(myList)
    revList = sorted(myList, reverse=True)
    
    for n in myList:
        for k in revList:
            for j in myList:
                if (int(n) + int(k) + int(j)) == 2020:
                    print("the product=",int(n) * int(k) * int(j))
                    break
            if (int(n) + int(k) + int(j)) == 2020:
                break
        if (int(n) + int(k) + int(j)) == 2020:
            break
    
