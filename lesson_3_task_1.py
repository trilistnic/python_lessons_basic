# task 1
def division(number_1, number_2):
    """Производит деление чисел"""
    try:
        result = number_1 / number_2
    except ZeroDivisionError:
        return 'Division by zero!'
    return result


var_1 = float(input('Введите число № 1: '))
var_2 = float(input('Введите число № 2: '))
print(f'Результат деления: {division(var_1, var_2):.2f}')