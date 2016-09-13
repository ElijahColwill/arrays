def haveThree(a):
    threes = 0
    for(i = 0; i < len(a); i += 1):
        if (a[i] == 3):
            threes += 1
    return threes == 3
