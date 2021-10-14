# task 2
from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    def __init__(self, size, height):
        self.size = float(size)
        self.height = float(height)

    @abstractmethod
    def square(self):
        pass


class Coat(MyAbstractClass):
    def square(self):
        return self.size * 6.5 + 0.5


class Suit(MyAbstractClass):
    def square(self):
        return self.height * 2 + 0.3


class Total_Square(MyAbstractClass):
    @property
    def square(self):
        print(f'Суммарный расход ткани: {Coat.square(self) + Suit.square(self)}')


size_c = input('Введите размер пальто: ')
height_s = input('Введите рост костюма: ')
total_square = Total_Square(size_c, height_s)
total_square.square