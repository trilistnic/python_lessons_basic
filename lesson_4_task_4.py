# task 4
numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_numbers = [i for i in numbers if numbers.count(i) == 1]

print(f'Исходный список: {numbers}')
print(f'Измененный список: {new_numbers}')