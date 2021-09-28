# task 5
def addition():
    numbers = []
    result = 0
    while numbers != 'end':
        data = input('Введите числа через пробел (для выхода введите - ):').split(' ')
        for i in data:
            try:
                if i != '-':
                    numbers.append(int(i))
                    result = sum(numbers)
                else:
                    numbers = 'end'
            except ValueError:
                return print('Неправильный ввод')
        print(f'Сумма введенных чисел: {result}')
    return result


addition()