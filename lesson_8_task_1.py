# task 1
class Date:
    day = 0
    month = 0
    year = 0

    def __init__(self, data):
        data.self = data

    @classmethod
    def date_transform(cls, data):
        try:
            Date.day, Date.month, Date.year = map(int, data.split('-'))
        except ValueError:
            pass

    @staticmethod
    def date_check():
        if 0 < Date.day < 32 and 0 < Date.month < 13 and 0 < Date.year < 2022:
            print(f'Введены число: {Date.day}, месяц: {Date.month}, год: {Date.year}')
        else:
            print('Введены некоректные данные')


info = input('Введите дату в формате дата-месяц-год: ')
Date.date_transform(info)
Date.date_check()