# task 1
from time import sleep


class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 10}
    work = 'working'

    def __init__(self):
        if list(TrafficLight.__color.keys()) != ['Красный', 'Желтый', 'Зеленый']:
            TrafficLight.work = 'broken' and print('Светофор сломан')
            return
        print('Настройка светофора!!!')
        for color, time_count in TrafficLight.__color.items():
            if input(f'{color} будет гореть: {time_count} (y/n)?:') == 'n':
                TrafficLight.__color[color] = int(input('Введите секунды: '))
            else:
                print(f'Выбрано значение по умолчанию: {time_count}')

    def running(self):
        for color, time_count in TrafficLight.__color.items():
            while time_count > 0:
                print(f'Сейчас горит: {color} {time_count}')
                time_count -= 1
                sleep(1)


road_light = TrafficLight()
if road_light.work == 'working':
    road_light.running()