# task 5
from functools import reduce


def multiplication(number_1, number_2):
    return number_1 * number_2


print(f'Результат перемножения: {reduce(multiplication, [i for i in range(100, 1001) if i % 2 == 0])}')