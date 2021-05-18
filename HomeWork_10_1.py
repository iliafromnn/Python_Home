class Matrix:
    def __init__(self, input_data):
        self.input = input_data
    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])
    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Несоответсвие размеров'
                sumline = [x + y for x, y in zip(line_1,line_2)]
                answer += ' '.join(map(str, sumline)) + '\n'
        else:
            return 'Несоответсвие размеров'
        return answer

matrix_1 = Matrix([[7, 8], [14, 5], [6, 18], [9, 5]])
matrix_2 = Matrix([[4, 12], [8, 18], [2, 1], [0, 20]])
print(matrix_1)
print()
print(matrix_1 + matrix_2)
