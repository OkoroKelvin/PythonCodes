# collection
# counter, named turple, OrderdDict, deafultdict,deque

from collections import Counter
"""
This function helps to display the numbers of apppearance of our elements.
It appears inform of keys and value(dictionaries)
"""
a = "aaaaabbbbcccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0])

b = "aaaaabbbbcccc"
my_counter_2 = Counter(b)
print(list(my_counter_2.elements()))


from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt)
print(pt.x,pt.y)
# https://pythongeeks.org/namedtuple-in-python/#:~:text=The%20namedtuple%20in%20Python%20is%20a%20function%20available,be%20accessed%20using%20either%20labels%20or%20normal%20indexing.
