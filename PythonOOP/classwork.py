square = ["One", "Two", "Three", "Four", "Five"]
dictionary = {}

vau = 0
for sq in square:
    values = [1, 2, 3, 4, 5]
    dictionary.update({sq: (values[vau])**2})
    vau = vau + 1
print(dictionary)


member_names = input("The names of member")

dictionary = {}

# while len(member_names):
while True:
    group_number = int(input("The input number"))
    amount_of_names = int(input("kindly type in number names"))
    names_list = []
    for i in range(amount_of_names):
        print(f'type name {i + 1}')
        member_names = input()
        names_list.append(member_names)

    dictionary.update({group_number: names_list})

    print(dictionary)

