tlds = {'Canada': 'ca', 'United States': 'us',
        'Mexico': 'mx'}
"""
a) Check whether the dictionary contains the key 'Canada'.
b) Check whether the dictionary contains the key 'France'.
"""
print('Canada' in tlds)
print('France' in tlds)


"""
c) Iterate through the key–value 
pairs and display them in two-column format"""
for values in tlds.keys():
    print(values,)


"""
d) Add the key–value pair 
'Sweden' and 'sw' (which is incorrect).
e) Update the value for the key 'Sweden' to 'se'.
"""

tlds['Sweden'] = 'sw'
print(tlds)
tlds.update({'Sweden':'se'})
print(tlds)
"""
f) Use a dictionary 
 to reverse the keys and values.
"""

tlds2 = {abbrv: country for country, abbrv in tlds.items()}
print(tlds2)

"""g) With the result of part (f), use a dictionary 
comprehension to convert the country names to
 all uppercase letters."""

tlds2 = {abbrv: country.upper() for country, abbrv in tlds.items()}
print(tlds2)