# task 1
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_view = ''
        for line in self.matrix:
            matrix_view = matrix_view + ' '.join(map(str, line)) + '\n'
        return matrix_view

    def __add__(self, other):
        result = []
        for line in range(max(len(self.matrix), len(other.matrix))):
            new_line = []
            for element in range(max(len(self.matrix[0]), len(other.matrix[0]))):
                try:
                    new_line.append(self.matrix[line][element] + other.matrix[line][element])
                except IndexError:
                    if len(self.matrix) > len(other.matrix) or len(self.matrix[0]) > len(other.matrix[0]):
                        new_line.append(self.matrix[line][element])
                    else:
                        new_line.append(other.matrix[line][element])
            result.append(new_line)
        return result


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
matrix_1 = Matrix(data)
matrix_2 = Matrix(data_2)
print(f'Матрица 1:\n{matrix_1}')
print(f'Матрица 2:\n{matrix_1}')
data_total = matrix_1 + matrix_2
matrix_total = Matrix(data_total)
print(f'Сумма матриц:\n{matrix_total}')