# task 5
proceeds = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
delta = proceeds - costs

if delta > 0 and costs > 0:
    efficiency = 100 * delta / proceeds
    print(f'Вы работаете с прибылью: {delta}, рентабельность выручки: {efficiency:.1f}%')
    employees = int(input('Введите количество сотрудников фирмы фирмы: '))
    print(f'Прибыль на сотрудника: {delta / employees:.2f}')
elif delta == 0:
    print('Маржинальность бизнеса = 0')
else:
    print(f'Вы работаете с убытками: {abs(delta)}')