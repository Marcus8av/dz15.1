# Возьмите любые задания из прошлых домашних заданий. 
# Добавьте к ним логирование ошибок и полезной информации.
# Дополнительно: реализуйте ввод из командной строки.

import logging

logging.basicConfig(filename='matrix.log', encoding='utf-8', level=logging.ERROR , filemode='w')

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in row]) for row in self.matrix])

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return False

    def __add__(self, other):
        if isinstance(other, Matrix) and len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(
                other.matrix[0]):
            result = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(result)
        else:
            logging.error("Матрицы должны быть одинакового размера для сложения!")
            raise ValueError("Матрицы должны быть одинакового размера для сложения!")

    def __mul__(self, other):
        if isinstance(other, Matrix) and len(self.matrix[0]) == len(other.matrix):
            result = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(other.matrix)):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(result)
        else:
            logging.error("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!")
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!")

    def print_info(self):
        print("Матрица:")
        print(self)

matrix1_input = []
matrix1_rows = int(input("Введите количество строк первой матрицы: "))
matrix1_cols = int(input("Введите количество столбцов первой матрицы: "))
print("Введите элементы первой матрицы:")
for _ in range(matrix1_rows):
    row = list(map(int, input().split()))
    matrix1_input.append(row)

matrix2_input = []
matrix2_rows = int(input("Введите количество строк второй матрицы: "))
matrix2_cols = int(input("Введите количество столбцов второй матрицы: "))
print("Введите элементы второй матрицы:")
for _ in range(matrix2_rows):
    row = list(map(int, input().split()))
    matrix2_input.append(row)

matrix1 = Matrix(matrix1_input)
matrix2 = Matrix(matrix2_input)

print("Первая матрица:")
print(matrix1)
print("Вторая матрица:")
print(matrix2)

print("Cравнение матриц:")
print(matrix1 == matrix2)

print("Cложение матриц:")
try:
    matrix3 = matrix1 + matrix2
    matrix3.print_info()
except ValueError as e:
    print(f"Ошибка: {e}")

print("Умножение матриц:")
try:
    matrix4 = matrix1 * matrix2
    matrix4.print_info()
except ValueError as e:
    print(f"Ошибка: {e}")