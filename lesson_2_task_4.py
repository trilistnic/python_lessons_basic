# task 4
data = str(input('Введите несколько слов через пробел: ')).split(' ')

for index, word in enumerate(data, 1):
    print(index, word[:10])