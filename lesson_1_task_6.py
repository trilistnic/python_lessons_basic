# task 6
distance = int(input('В первый день спортсмен пробежал км: '))
distance_target = int(input('Цель пробежать км: '))
if distance <= 0 or distance_target <= 0:
    print('Так не может быть!')
else:
    i = 1
    while distance < distance_target:
        distance *= 1.1
        i += 1

    print(f'На {i}-й день спортсмен достиг результата — не менее {distance_target}км.')