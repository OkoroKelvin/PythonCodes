mylist = ["banana", "cherry", "apple"]
print(mylist)

item = mylist[-1]
print(item)

# for i in mylist:
#     print(i)


if "banana" in mylist:
    print("yes")
else:
    print("no")

# to know length
print(len(mylist))

mylist.append("PawPaw")
mylist.append("Cassava")
mylist.append("Tomatoes")
print(mylist)

mylist.insert(1, "One_Nutrient")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

mylist.remove("cherry")
print(mylist)

# mylist.clear()
# print(mylist)

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

new_list = sorted(mylist)
print(new_list)

my_new_list = [0] * 5
print(my_new_list)
my_new_list2 = [1, 2, 3, 4, 5]
sum_list = my_new_list + my_new_list2
print(sum_list)

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = a_list[1:5]
print(a)
b = a_list[:5]
print(b)
c = a_list[1:]
print(c)
d= a_list[:]
print(d)
e= a_list[::2]
print(e)
f= a_list[::-1]
print(f)
list_org = ["Banana","Cherry","apple"]
list_cpy = list_org.copy()
list_cpy.append("Pepper Soup")
print(list_cpy)
print(list_org)

b_list = [1,2,3,4,5,6]
b = [i*i for i in b_list]
print(b_list)
print(b)