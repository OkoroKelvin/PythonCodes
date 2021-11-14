# Strings are ordered, immutable, text representation
my_string = """
Hello 
World
"""

print(my_string)

my_string = "Hello world"
kelvin = my_string[0:4]
print(kelvin)

# .strip() helps remove every spaces
My_string = '         hello        '
print(My_string.strip())
print(My_string.upper())

my_string = "Hello world"
print(my_string.endswith('world'))

print(my_string.find('o'))
print(my_string.count('o'))
print(my_string.replace('world', 'Universe'))

# To convert string to List
my_string = 'how are you doing'
my_list = my_string.split()
print(my_list)
my_string = 'how are you doing'
# By default theres a space..The split function finds spaces in the words and split from it
my_list = my_string.split(" ")
print(my_list)
# The one below will not split, because there are no spaces in betwwen
# Therefor the split function only works when its sees space
my_string = 'how,are,you,doing'
my_list = my_string.split(" ")
print(my_list)
# So if u want it to split, you add , to the split function
my_list2 = my_string.split(",")
print(my_list2)

my_string = 'how,are,you,doing'
my_list = my_string.split(",")
print(my_list)
new_string = ' '.join(my_list)
print(new_string)

my_list = ['a'] * 6
print(my_list)

# bad way of turning list to string
my_new_string = ''
for i in my_list:
    my_new_string += i
print(my_new_string)

# Good way of converting list to string
my_list = ['a'] * 6
my_new_string = ' '.join(my_list)
print(my_new_string)

# .format(),f-strings
