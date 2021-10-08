# task 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        _income = {'wage': wage, 'bonus': bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self.income = _income


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name + " " + self.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {sum(self.income.values())}')


try:
    data = Position(input('Имя:'), input('Фамилия:'), input('Должность:'), int(input('Оклад:')), int(input('Премия:')))
    data.get_full_name()
    data.get_total_income()
except ValueError:
    print('Данные некорректны!')