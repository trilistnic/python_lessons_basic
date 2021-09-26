# task 6
i = 1
titles = ['название', 'цена', 'количество', 'единица измерения']
list_data = []
dictionary_update = {}
while True:
    print('Для окончания записи введите: -')
    data = input(f'Товар {i} (название, цена, количество, единица измерения) через пробел:').split(' ')
    if data == ['-']:
        break
    dictionary = dict(zip(titles, data))
    list_data.append((i, dictionary))
    for key, value in dictionary.items():
        dictionary_update.setdefault(key, []).append(value)
    i += 1

print(f'Структура данных Товары: {list_data}')
print(f'Аналитика о товарах: {dictionary_update}')