peace_set = {'red', 'green', 'blue'}
fight_set = {'cyan', 'green', 'blue', 'magenta', 'red'}

# print(peace_set == fight_set)
# print(peace_set < fight_set)
# print(peace_set <= fight_set)
"""You may a so check for an improper 
subset with the set method issubset"""
# print(peace_set.issubset(fight_set))
#
# """
# The > operator tests whether the set to its left is a proper superset of the one to its
# right—that is, all the elements in the right operand are in the left operand, and the left
# operand has more elements:
# """
# print(peace_set > fight_set)
#
# print(peace_set.issuperset(fight_set))
#
# """Mathematical Set Operation"""
# print(peace_set.union(fight_set))
#
# print(peace_set.intersection(fight_set))

print(peace_set-fight_set)

