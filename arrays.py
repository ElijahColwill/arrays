def haveThree(a):
    threes = 0
    for num in a:
        if num == 3:
            threes += 1
    return threes == 3

print haveThree([3, 4, 3, 4, 3])
print haveThree([3, 5, 3,])

def sum28(b):
    sum = 0
    for num in b:
        if num == 2:
            sum += 1
    return sum == 4

print sum28([2, 2, 2, 2])
print sum28([2, 2, 2])
print sum28([2, 2])
print sum28([4, 2, 3, 2, 2, 2, 1])
