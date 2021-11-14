my_dict = {"name": "Max", "age": 28, "City": "New york"}
# print(my_dict)
#
# value = my_dict["name"]
# print(value)

my_dict2 = dict(name="Mary", age=27, city="Bostom")
print(my_dict2)

my_dict["name"] = "max@xyz.com"
print(my_dict)

del my_dict["name"]
print(my_dict)

my_dict.pop("age")
print(my_dict)

# The function below deletes the last added item
my_dict2.popitem()
print(my_dict2)

if "name" in my_dict2:
    print(my_dict2["name"])

try:
    print(my_dict2["Mary"])
except:
    print("Error")

# for key in my_dict2:
#     print(key)


for key in my_dict2.keys():
    print(key)

for value in my_dict2.values():
    print(value)

for key, value in my_dict2.items():
    print(key, value)

my_dict_cpy = my_dict2
print(my_dict_cpy)
my_dict_cpy["ziga"] = "Tina@youtbe.com"
print(my_dict2)

print(my_dict_cpy)

c_my_dict = {"name": "Tina", "Age": 34, "city": "japan"}
c_my_dict_cpy = c_my_dict.copy()
c_my_dict_cpy["Club"] = "Press Club"
print(c_my_dict)
print(c_my_dict_cpy)

d_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
d_dict_2 = dict(name="Mary", age=27, city="Bostom")

d_dict.update(d_dict_2)
print(d_dict)

e_dict = {3: 9, 6: 36, 9: 81}
print(e_dict)

value = e_dict[3]
print(value)

myTuple = (8, 7)
edict = {myTuple: 15}
print(edict)
