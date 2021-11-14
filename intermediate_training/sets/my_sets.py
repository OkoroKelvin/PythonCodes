myset = {1, 2, 3, 4, 1, 1, 2}
# Set does not allow duplicates
# set is unordered
# set has no duplicate
print(myset)

a_myset = set([1, 2, 3, 3, 2])
print(a_myset)

b_myset = set("Hello")
print(b_myset)
b_myset.add(1)
b_myset.add(2)
print(b_myset)

b_myset.remove(2)
print(b_myset)

b_myset.discard("H")
print(b_myset)

for i in b_myset:
    print(i)

if 100 in b_myset:
    print("yes")
else:
    print("No")

odds = {1, 3, 5, 7, 9}
evens = {0, 3, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i2 = odds.intersection(primes)
print(i2)

i3 = evens.intersection(primes)
print(i3)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# This command below prints the numbers from setA that are not in setB
diff = setA.difference(setB)
print(diff)

# This command below prints the numbers from setB that are not in setA
diff2 = setB.difference(setA)
print(diff2)
"""this command below takes and prints element that are not 
common to both set..But skips elements that 
appears in both.
"""
diff3 = setB.symmetric_difference(setA)
print(diff3)
diff4 = setB.symmetric_difference(setA)
print(diff4)

setA.update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

"""this command below helps to keep only
common elements
"""
setA.intersection_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

"""
It removes common numbers in SetB from SetA
and leave the rest numbers in SetA  
"""
setA.difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
"""This removes the common elements of both sets and joins
the uncommon one together to form the new set
"""

setA.symmetric_difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
"""
This command(issubset) says all elements are in setA are in setB
if this is true, it prints True.
but if false, prints false
"""
print(setA.issubset(setB))
print(setB.issubset(setA))

"""
This command(issuperset) states that if firsSet has all memebers of second sets.
If the firstsaet has all secondset, then its a supperst to the secondset
Thereby returns true...if other wise returns false
"""
print(setA.issuperset(setB))
print(setB.issuperset(setA))

"""
This command throws true if there is no common element betw the first and second set
And throws false if they are common elements
"""
print(setA.isdisjoint(setB))

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}

print(setA.isdisjoint(setC))
setB = setA

setB.add(7)
print(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}

setC = setA.copy()
setC.add(9)
# This command below helps creat a copy of setA to setB
setB = set(setA)


# You can not change a frozen set
a = frozenset([1, 2, 3, 4])
