# task 2
data = str(input('Введите элементы списка через пробел: ')).split(' ')

for i in range(len(data) - 1):
    if len(data) > 1 and i % 2 == 0:
        data[i], data[i + 1] = data[i + 1], data[i]

print(f'Список с обменом значений соседних элементов: {data}')