# 6.5 (Counting Duplicate Words) Write a script that uses a dictionary to determine and
# print the number of duplicate words in a sentence. Treat uppercase and lowercase letters
# the same and assume there is no punctuation in the sentence. Use the techniques you
# learned in Section 6.2.7. Words with counts larger than 1 have duplicates.

my_text = 'The Lord is my rock and my Life, I will trust in Him forevermore. Lord please lord me'
new_text = my_text.upper()
dict_word = {}
each_words = new_text.split()
for words in each_words:
    if words in dict_word:
        dict_word[words] += 1

    else:
        dict_word[words] = 1

for ask, team in sorted(dict_word.items()):
    print(f'{ask} appears {team} times')
