# task 2
with open('input.txt', 'r') as file:
    i = 1
    for line in file:
        print(f'В строке {i}: {len(line)} символов')
        i += 1
    print(f'Количество строк в {file.name}: {i}')