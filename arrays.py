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

def countEvens(c):
    even = 0
    for nums in c:
        if nums % 2 == 0:
            even += 1
    return even

print "--"
print countEvens([2, 1, 2, 3, 4])
print countEvens([2, 2, 0])
print countEvens([1, 3, 5])
