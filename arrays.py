the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "This is count %d" % number


for fruit in fruits:
    print "A fruit of type: %s" % fruit

for i in change:
    print "I got %r" % i

elements = []

for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)

for i in elements:
    print "Element was: %d" % i

pizza = []

for i in range(0, 13):
    print "Number of pizza slics: %d" % i
    pizza.append(i)

for i in pizza:
    print "Slices eaten: %d" % i

def countEvens(array0):
    even = 0
    for nums in array0:
        if nums % 2 == 0:
            even += 1
    return even

print "--"
print countEvens([2, 1, 2, 3, 4])
print countEvens([2, 2, 0])
print countEvens([1, 3, 5])

def bigDiff(array1):
    return max(array1) - min(array1)

print "--"
print bigDiff([10, 3, 5, 6])
print bigDiff([7, 2, 10, 9])
print bigDiff([2, 10, 7, 2])

def centeredAverage(array2):
    array2.sort()
    trimmed = array2[1:-1]
    return sum(trimmed)/len(trimmed)

print "--"
print centeredAverage([1, 2, 3, 4, 100])
print centeredAverage([1, 1, 5, 5, 10, 8, 7])
print centeredAverage([-10, -4, -2, -4, -2, 0])

def sum13(array3):
    if len(array3) == 0:
        return 0
    skipnext = False
    sum = 0
    for i in array3:
         if i == 13:
             skipnext = True
             continue
         if skipnext:
             skipnext = False
             continue
         else: sum += i
    return sum

print "--"
print sum13([1, 2, 2, 1])
print sum13([1, 1])
print sum13([1, 2, 2, 1, 13])
print sum13([1, 2, 2, 1, 13, 13, 13, 13, 1, 2])

def sum67(array4):
    if len(array4) == 0:
        return 0
    startswith6 = False
    sum = 0
    for i in array4:
        if not startswith6:
            if i == 6:
                startswith6 = True
            else: sum += i
        elif i == 7:
            startswith6 = False
    return sum

print "--"
print sum67([1, 2, 2])
print sum67([1, 2, 2, 6, 99, 99, 99, 7, 1])
print sum67([1, 1, 6, 7, 2])

def has22(array5):
    nextto2 = False
    final = False
    for i in array5:
        if nextto2:
            if i == 2:
                final = True
            else: nextto2 = False
        elif not nextto2:
            if i == 2:
                nextto2 = True
    return final == True

print "--"
print has22([1, 2, 2])
print has22([1, 2, 1, 2])
print has22([2, 1, 2])

def lucky13(array6):
    detected1or3 = False
    for i in array6:
        if i == 1:
            detected1or3 = True
        if i == 3:
            detected1or3 = True
    return not detected1or3

print "--"
print lucky13([0, 2, 4]) # True
print lucky13([1, 2, 3]) # False
print lucky13([1, 2, 4]) # False

def sum28(array7):
    twos = 0
    for i in array7:
        if i == 2:
            twos += 1
    return twos == 4

print "--"
print sum28([2, 3, 2, 2, 4, 2]) # True
print sum28([2, 3, 2, 2, 4, 2, 2]) # False
print sum28([1, 2, 3, 4]) # False

def more14(array8):
    ones = 0
    fours = 0
    for i in array8:
        if i == 1:
            ones += 1
        if i == 4:
            fours += 1
    return ones > fours

print "--"
print more14([1, 4, 1]) # True
print more14([1, 4, 1, 4]) # False
print more14([1, 1]) # True

def fizzArray(n):
    array9 = []
    for i in range(n):
        array9.append(i)
    return array9

print "--"
print fizzArray(4)
print fizzArray(1)
print fizzArray(10)
print fizzArray(0)

def only14(array10):
    total = len(array10)
    all14 = 0
    for i in array10:
        if i == 1:
            all14 += 1
        if i == 4:
            all14 += 1
    return total == all14

print "--"
print only14([1, 4, 1, 4]) # True
print only14([1, 4, 2, 4]) # False
print only14([1, 1]) # True

def fizzArray2(n):
    array11 = []
    for i in range(n):
        i = str(i)
        array11.append(i)
    return array11

print "--"
print fizzArray2(4)
print fizzArray2(10)
print fizzArray2(2)


def sum13_2(array13):
    sum = 0
    for i in range(0, len(array13)):
        if i == (len(array13) - 1):
            if array13[i] != 13:
                sum += array13[i]
            else:
                if array13[i] == 13:
                    sum -= array13[i + 1]
                else:
                    sum += array13[i]
    return sum

print "--"
print sum13_2([1, 2, 2, 1])
print sum13_2([1, 1])
print sum13_2([1, 2, 2, 1, 13])
print sum13_2([1, 2, 2, 1, 13, 13, 13, 13, 1, 2])
