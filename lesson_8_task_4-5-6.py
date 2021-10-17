# task 4
class Warehouse:
    def __init__(self):
        self._data = {}
        self._department = {}

    def inspection(self, hard_eq):
        self._data.setdefault(hard_eq.group, []).append(hard_eq)

    def department(self, name, department):
        if self._data[name]:
            self._department.setdefault(department, []).append({name: self._data[name][0]})
            self._data.setdefault(name).pop(0)

    @staticmethod
    def info():
        try:
            number = int(input('Что добавляем на склад? (принтер -1 ; сканер - 2 ; ксерокс - 3 ): '))
            name = input('Введите название фирмы: ')
            year = input('Введите год производства: ')
            if number == 1:
                data.inspection(Printer(name, year))
            elif number == 2:
                data.inspection(Scanner(name, year))
            elif number == 3:
                data.inspection(Xerox(name, year))
            else:
                print('Ввести можно 1, 2 или 3')
        except ValueError:
            print('Введено не число!')


class Equipment(Warehouse):
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.group = self.__class__.__name__

    def counting(self):
        pass

    def __repr__(self):
        return f'{self.name} {self.year}'


class Printer(Equipment):
    count = 0

    def __init__(self, name, year):
        super().__init__(name, year)

    def counting(self):
        Printer.count += 1
        return Printer.count


class Scanner(Equipment):
    count = 0

    def __init__(self, name, year):
        super().__init__(name, year)

    def counting(self):
        Scanner.count += 1
        return Scanner.count


class Xerox(Equipment):
    count = 0

    def __init__(self, name, year):
        super().__init__(name, year)

    def counting(self):
        Xerox.count += 1
        return Xerox.count


data = Warehouse()
data.inspection(Printer('HP', 2010))
data.inspection(Printer('Canon', 2011))
data.inspection(Scanner('DELL', 2012))
data.inspection(Scanner('Leica', 2013))
data.inspection(Xerox('Xerox', 2014))
data.inspection(Xerox('Ecosys', 2015))
print(f'На складе: {data._data}')
data.department('Scanner', 'Отдел 1')
data.department('Printer', 'Отдел 1')
data.department('Xerox', 'Отдел 1')
data.department('Xerox', 'Отдел 2')
print(f'Передали в отделы: {data._department}')
print(f'На складе: {data._data}')
data.info()
print(f'На складе: {data._data}')