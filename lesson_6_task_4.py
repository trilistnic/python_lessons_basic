# task 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_left(self):
        print(f'{self.name} повернула налево')

    def turn_right(self):
        print(f'{self.name} повернула направо')

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} Превышает допустимую скорость на: {self.speed - 60}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} Превышает допустимую скорость на: {self.speed - 40}')

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def check_police(self):
        if self.is_police:
            print(f'{self.name} полицейская машина')


Lamborghini = SportCar(200, 'white', 'Lamborghini', False)
Citroen = TownCar(80, 'black', 'Citroen', False)
Volkswagen = WorkCar(30, 'green', 'Volkswagen', False)
Ford = PoliceCar(100, 'blue', 'Ford', True)
print(f'{Lamborghini.color} {Lamborghini.name} moving with {Lamborghini.speed}')
Ford.check_police()
Citroen.go()
Citroen.stop()
Volkswagen.turn_left()
Volkswagen.turn_right()
print(f'{Volkswagen.name} is police?: {Volkswagen.is_police}')
Volkswagen.show_speed()
Citroen.show_speed()