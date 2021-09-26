# task 3
month = int(input('Введите номер месяца: '))

m = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
season_dict = {"зима": [1, 2, 12],
               "весна": [3, 4, 5],
               "лето": [6, 7, 8],
               "осень": [9, 10, 11]}


def season(month_number):
    for key, value in season_dict.items():
        if month_number in value:
            return key


if 0 < month < 13:
    print(f'{m[month - 1]} - это: {season(month)}')
else:
    print('Номер месяца от 1 до 12')