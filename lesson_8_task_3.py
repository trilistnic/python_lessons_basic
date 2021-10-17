# task 3
class Checker(Exception):
    @staticmethod
    def list_check():
        number = ''
        result = []
        while number != 'stop':
            number = input('Введите число (для выхода введите stop):')
            try:
                if number[:1] == '-' and str(number[1:]).isdigit() or str(number).isdigit():
                    result.append(number)
                elif number == 'stop':
                    print('Введено слово stop -> окончание программы')
                else:
                    raise Checker("Вы ввели текст!")
            except Checker as err:
                print(err)
        print(result)


Checker.list_check()