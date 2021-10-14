# task 3
class Cell:
    count = 1

    def __init__(self, number, cells_row):
        self.number = number
        self.cells_row = cells_row
        if number <= 0 or cells_row <= 0:
            raise RuntimeError('Введенное число не может быть < = 0')

    def __add__(self, other):
        return f'Результат сложения: {self.number + other.number}'

    def __sub__(self, other):
        return f'Результат вычитания: {self.number - other.number if self.number > other.number else "Отрицательное"}'

    def __mul__(self, other):
        return f'Результат умножения: {self.number * other.number}'

    def __truediv__(self, other):
        return f'Результат деления: {self.number // other.number}'

    def make_order(self):
        print(f'Структура клетки №{Cell.count}: ')
        Cell.count += 1
        return str(self.number // self.cells_row * (self.cells_row * '*' + '\\n') + self.number % self.cells_row * '*')


try:
    cell_1 = int(input('Введите число ячеек клетки №1:'))
    order_1 = int(input('Введите оличество ячеек в ряду клетки №1:'))
    cell_2 = int(input('Введите число ячеек клетки №2:'))
    order_2 = int(input('Введите оличество ячеек в ряду клетки №2:'))
except ValueError:
    print('Не число')

cell_1 = Cell(cell_1, order_1)
cell_2 = Cell(cell_2, order_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order())
print(cell_2.make_order())