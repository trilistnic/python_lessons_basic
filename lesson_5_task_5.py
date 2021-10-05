# task 5
def total(file_name):
    with open(file_name, 'a+') as file:
        data = input('Введите числа через пробел: ')
        file.writelines(data)
        file.seek(0)
        data = file.readline().split(' ')
        try:
            result = sum(map(int, data))
        except ValueError:
            return print('Неправильный ввод')
        print(f'Сумма введенных чисел: {result}')


total('total.txt')