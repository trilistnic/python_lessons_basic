# task 2
class Road:
    thickness = 5
    mass_1sm = 25

    def __init__(self, _length, _width):
        self.len = _length
        self.wid = _width
        if input(f'Масса асфальта для 1 кв метра дороги, толщиной в 1 см: {Road.mass_1sm} (y/n)?:') == 'n':
            Road.mass_1sm = input('Введите значение: ')
        else:
            print(f'Выбрано значение по умолчанию: {Road.mass_1sm}')
        if input(f'Толщина полотна в см: {Road.thickness} (y/n)?:') == 'n':
            Road.thickness = input('Введите значение: ')
        else:
            print(f'Выбрано значение по умолчанию: {Road.thickness}')

    def mass(self):
        try:
            result = int(Road.thickness) * int(Road.mass_1sm) * int(self.len) * int(self.wid) / 1000
            print(f'Масса асфальта: {result} тонн(ы)')
        except ValueError:
            return print('Ошибка в введенных значениях')


road_mass = Road(input('Введите длину полотна (м): '), input('Введите ширину полотна (м): '))
road_mass.mass()