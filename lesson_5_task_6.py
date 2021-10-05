# task 6
lecture = {}
with open('input.txt', 'r') as file:
    for line in file:
        subject, time = line.split(':')
        time = ''.join((i if str(i).isdigit() else ' ') for i in time).split()
        lecture[subject] = sum(map(int, time))
    print(f'Общее количество занятий: {lecture}')