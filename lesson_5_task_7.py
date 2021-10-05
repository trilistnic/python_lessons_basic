# task 7
import json
firm = {}
with open('input.txt', 'r') as file:
    for line in file:
        try:
            name, form, proceeds, expenses = line.split()
            firm[name] = int(proceeds) - int(expenses)
        except ValueError:
            print('Ошибка данных в файле')
average = {'average_profit': sum(i for i in firm.values() if i > 0) / sum(1 for i in firm.values() if i > 0)}
with open("input.json", "w") as write_file:
    json.dump([firm] + [average], write_file)