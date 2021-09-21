# task 4
number = int(input('Введите число: '))
check = -1
if number < 0:
    print(f'Число {number} отрицательное!!!')
    number = int(input('Введите число: '))

while number >= 1:
    number_remain = number % 10
    number //= 10
    if number_remain > check:
        check = number_remain

print('Самая большая цифра в числе: ', check)