# task 4
def degree(var_1, var_2):
    """Возводит число 1 в степень числа 2"""
    return var_1 ** var_2


number_1 = float(input('Введите действительное положительное число: '))
number_2 = int(input('Введите целое отрицательное число: '))

print(f'Число {number_1} в степени {number_2} равно:{degree(number_1, number_2)}')

"""
# task 4 2 way
def degree(var_1, var_2, result):
    """Возводит число 1 в степень числа 2"""
    for i in range(1, abs(var_2)):
        result *= var_1
    return 1 / result


number_1 = float(input('Введите действительное положительное число: '))
number_2 = int(input('Введите целое отрицательное число: '))

if number_2 < 0:
    print(f'Число {number_1} в степени {number_2} равно:{degree(number_1, number_2, result = number_1)}')
else:
    print(f'Число {number_2} не отрицательное')
"""