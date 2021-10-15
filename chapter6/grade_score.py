grade_book = {
    'Susan': [92, 85, 100],
    'Eduardo': [83, 95, 79],
    'Aziz': [91, 89, 82],
    'Patina': [97, 91, 92]
}
total = 0
total_length = 0
for name, scores in grade_book.items():
    average_score = (sum(scores))/(len(scores))
    print(f'{name} average score is {average_score:.2f}')
    total = total+sum(scores)
    total_length += len(scores)
total_average = total/total_length
print(f'The total score in calss is {total_average:.2f}')
