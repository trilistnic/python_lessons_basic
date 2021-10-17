# task 2
class Zero_Division(Exception):
    @staticmethod
    def division(number_1, number_2):
        try:
            if int(number_2) == 0:
                raise Zero_Division("Вы ввели 0, как делитель!")
            division = int(number_1) / int(number_2)
            print(f'Результат деления: {division}')
        except ValueError:
            print("Вы ввели не число")
        except Zero_Division as err:
            print(err)


Zero_Division.division(input('Введите делимое: '), input('Введите делитель: '))