# task 1
from sys import argv

script_name, output, rate, bonus = argv

try:
    print(f'Заработная плата сотрудника: {int(output) * int(rate) + int(bonus)}')
except ValueError:
    print('Введено не число!')
