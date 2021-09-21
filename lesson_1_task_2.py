# task 2
def formatted(number):
    if number in range(0, 9):
        number = str(0) + str(number)
    return number


seconds = int(input('Введите время в секундах: '))
hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
seconds = seconds - minutes * 60 - hours * 3600
print(f'Отформатированное время: {formatted(hours)}:{formatted(minutes)}:{formatted(seconds)}')