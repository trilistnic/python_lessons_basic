# task 3
def my_func(var_1, var_2, var_3):
    elements = [var_1, var_2, var_3]
    return sum(elements) - min(elements)


number_1 = float(input('Введите число №1: '))
number_2 = float(input('Введите число №2: '))
number_3 = float(input('Введите число №3: '))

print(f'Сумма наибольших двух чисел из введенных: {my_func(number_1, number_2, number_3):.2f}')