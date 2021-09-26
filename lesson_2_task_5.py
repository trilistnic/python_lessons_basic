# task 5
my_list = [7, 5, 3, 3, 2]
data = int(input('Введите новое число рейтинга: '))
index = -1

for position, number in enumerate(my_list):
    if number >= data:
        index = position

my_list.insert(index + 1, data)
print(my_list)