with open('grades.tx', 'r') as grades:
    print(f'number   grade_name   grade_score')
    for grade in grades:
        number, grade_name, grade_score = grade.split()
        print(f'{number}   {grade_name}   {grade_score}')
