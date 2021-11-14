mytuple = "Max", 28, "Boston"
print(type(mytuple))
a_tuple = tuple(["Max", 28, "Bostom"])
print(a_tuple)
print(type(a_tuple))

for i in a_tuple:
    print(i)

b_tuple = ('a', 'p', 'p', 'l', 'e')
print(b_tuple.count('p'))
print(b_tuple.index('l'))

my_list = list(b_tuple)
print(my_list)

c_tuple = tuple(my_list)
print(c_tuple)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[0:5]
print(b)

my_tuple = "Max", 28, "Boston"
name, age, city = my_tuple
print(name)
print(age)
print(city)

i1, *i2, i3 = a
print(i1)
print(i2)
print(i3)

import sys

c_list = [0, 1, 2, "hello", True]
c_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(mytuple), "bytes")

import timeit

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))

