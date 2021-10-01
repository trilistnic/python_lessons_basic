# task 6
from itertools import count, cycle
start = int(input('Введите число, с которого нужно начать: '))
end = int(input('Введите число, которым нужно закончить: '))

for number in count(start):
    if number > end:
        break
    else:
        print(number)

stop = 1
elements = '12345'
value = int(input(f'Введите сколько раз нужно повторить {elements}: '))
for number in cycle(elements):
    if stop > value * len(elements):
        break
    print(number)
    stop += 1