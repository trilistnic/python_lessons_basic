# task 7
def fact(number):
    """Подсчитывает факториал числа"""
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
        yield factorial, i


n = int(input('Введите число, до которого нужно вывести факториалы: '))
for el, position in fact(n):
    print(f'Факториал !{position} равен: {el}')