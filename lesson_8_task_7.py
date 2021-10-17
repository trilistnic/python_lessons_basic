# task 7
class Complex:
    def __init__(self, num_1, num_2, *args):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        print(f'Сумма комплексных чисел равна: ')
        return f'{self.num_1 + other.num_1} + {self.num_2 + other.num_2} * i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел равно: ')
        return f'{self.num_1 * other.num_1 - self.num_2 * other.num_2} + {self.num_1 * other.num_2 + self.num_2 * other.num_1} * i '

    def __str__(self):
        return f'{self.num_1} + {self.num_2} * i'


number_1 = Complex(1, -2)
number_2 = Complex(3, 4)
print(number_1)
print(number_2)
print(number_1 + number_2)
print(number_1 * number_2)