# task 4
def numbers_change(file_name):
    with open(file_name, 'r') as file:
        i = 0
        numbers = ['Один ', 'Два ', 'Три ', 'Четыре ']
        try:
            for line in file:
                surname, salary = line.split('-')
                surname = numbers[i]
                i += 1
                with open('new_'+file_name, 'a') as new_file:
                    new_file.write(f'{surname}-{salary}')
        except ValueError:
            return print('Ошибка данных в файле')


numbers_change('numbers.txt')