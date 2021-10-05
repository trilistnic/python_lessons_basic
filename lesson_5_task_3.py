# task 3
def salary_count(file_name):
    with open(file_name, 'r') as file:
        workers = []
        money = 0
        amount = 0
        try:
            for line in file:
                surname, salary = line.split(' ')
                money += int(salary)
                amount += 1
                if int(salary) < 20000:
                    workers.append(surname)
            print(f'Сотрудники с окладом меньше 20.000: {workers}, средний оклад: {money / amount}')
        except ValueError:
            return print('Ошибка данных в файле')


salary_count('salary.txt')