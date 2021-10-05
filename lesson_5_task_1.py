# task 1
line = 'start'
with open('input.txt', 'w') as file:
    while line:
        line = input('Введите текст: ')
        file.write(line + '\n')