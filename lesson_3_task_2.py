# task 2
def output(var_1, var_2, var_3, var_4, var_5):
    """Выводит запрошенные данные"""
    print(f'Имя: {var_1} Фамилия: {var_2} Год рождения: {var_3} Город проживания: {var_4} email: {var_5}')


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')

output(var_1=name, var_2=surname, var_3=year, var_4=city, var_5=email)

""" 
# task 2 2 way
def output(var_1, var_2, var_3, var_4, var_5):
    """Выводит запрошенные данные"""
    return ' '.join([var_1, var_2, var_3, var_4, var_5])


print(output(var_1='Ivan', var_2='Ivanov', var_3='2000', var_4='NY', var_5='ivan@ivanov.com'))
"""