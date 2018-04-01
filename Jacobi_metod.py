import copy
import math


def get_size():
    n = int(input('Введіть кількість рядків квадратної матриці '))
    return n


n = get_size()


def get_matrix():
    global n
    matrix = [[0.0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = float(input(('Введіть  елемент ' + str(i + 1) + ' рядка ' + str(j+1) + ' стовпця матриці ')))
    return matrix


def print_matrix(mat):
    global n
    for i in range(0, n):
        print(mat[i])

    print(" ")


def get_vector(type):
    global n
    b = [1 for i in range(n)]
    for i in range(0, n):
        b[i] = float(input(('Введіть ' + str(i+1) + ' елемент вектора ' + type + ' ')))
    return b


def sum_of_matrix(mat1,mat2):

    for i in range(0, n):
        for j in range(0, n):
            mat1[i][j] += mat2[i][j]

    return mat1


def sum_of_vectors(v1, v2):
    for i in range(n):
        v1[i] += v2[i]
    return v1


def multiplication(a, b):
    global n
    result = [[0.0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def scalar_multiplication(matrix, b):
    global n
    result = copy.deepcopy(matrix)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] *= b
    return result


def matrix_times_vector(matrix, vector):
    result = [0 for i in range(n)]

    for i in range(0, n):
        for j in range(0, n):
            result[i] += matrix[i][j]*vector[j]
    return result


def norm(v1, v2):
    s = 0
    for i in range(n):
        s += math.pow(v1[i] - v2[i], 2)
    s = math.sqrt(s)
    return s


def decomposition(matrix):
    lower = copy.deepcopy(matrix)
    upper = copy.deepcopy(matrix)
    diagonal = copy.deepcopy(matrix)

    for i in range(0, n):
        for j in range(0, n):
            if i <= j:
                lower[i][j] = 0

    for i in range(0,n):
        for j in range(0, n):
            if i >= j:
                upper[i][j] = 0

    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                diagonal[i][j] = 0

    return lower, upper, diagonal


def invert_diagonal_matrix(matrix):
    for i in range(0, n):
        matrix[i][i] = 1/matrix[i][i]
    return matrix


A = get_matrix()
print_matrix(A)
L, R, D = decomposition(A)
D_inverse = invert_diagonal_matrix(D)
B = multiplication(scalar_multiplication(D_inverse, -1), sum_of_matrix(L, R))

eps = 0.0001
b = get_vector('значень')
a = [0.001 for i in range(n)]
for i in range(10000):
    x =[[0 for k in range(n)] for m in range(i+1)]
    x[0] = a
    for j in range(0, i):
        x[j] = sum_of_vectors(matrix_times_vector(B, x[j - 1]), matrix_times_vector(D_inverse, b))
        if norm(x[j], x[j-1]) >= eps:
            x[j+1] = sum_of_vectors(matrix_times_vector(B, x[j]), matrix_times_vector(D_inverse, b))
        else:
            answer = x[j]
            for k in range(0,n):
                print('X' + str(k+1) + "= " + str(round(answer[k], 3)))
            print('Отримано на ' + str(j) + '-й ітерації')
            quit()


