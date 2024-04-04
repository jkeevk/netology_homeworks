dicts = {'Python': [9, 4, 7, 3], 'Git': [3, 6, 2, 5]}
def get_average_grade(dicts):
    result = 0
    ammount = 0
    for i in dicts.values():
        for j in i:
            ammount += 1
            result += j
    average = result / ammount
    average = float('{:.1f}'.format(average))
    print(average)

result = f'оценка за лекции: {get_average_grade}'

get_average_grade(dicts)