# task 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Рисуем с помощью: {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Рисуем с помощью: {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Рисуем с помощью: {self.title}')


main = Stationery('канцтовар')
main.draw()
pen = Pen('ручки')
pen.draw()
pencil = Pencil('карандаша')
pencil.draw()
handle = Handle('маркера')
handle.draw()