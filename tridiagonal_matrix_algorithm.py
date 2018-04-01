def get_size():
    n = int(input('Введіть кількість рядків квадратної матриці '))
    return n


def get_matrix():
    global n
    matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = float(input(('Введіть  елемент ' + str(i + 1) + ' рядка ' + str(j+1) + ' стовпця матриці ')))
    return matrix


def get_vector(type):
    global n
    b = [1 for i in range(n)]
    for i in range(0, n ):
        b[i] = float(input(('Введіть ' + str(i+1) + ' елемент вектора ' + type + ' ')))
    return b


def print_matrix(mat):
    global n
    for i in range(0,n):
        print(mat[i])


def tridiag_solv(matrix, d):
    global n
    alpha = [0 for i in range(n-1)]
    betha = [0 for i in range(n)]
    x = [0 for i in range(n)]

    alpha[0] = matrix[0][1]/matrix[0][0]
    for i in range(1,n-1):
        alpha[i] = matrix[i][i+1]/(matrix[i][i] - matrix[i][i-1]*alpha[i-1])

    betha[0] = d[0]/matrix[0][0]
    for i in range(1, n):
        betha[i] = (d[i] - matrix[i][i-1]*betha[i-1])/(matrix[i][i] - matrix[i][i-1]*alpha[i-1])

    x[n-1] = betha[n-1]
    for i in range (n-2, -1,-1):
        x[i] = betha[i] - alpha[i]*x[i+1]

    for i in range(0,n):
        print("x " + str(i) + " = " + str(round(x[i], 2)))


n = get_size()
matrix = get_matrix()

d = get_vector('значень')
print_matrix(matrix)

tridiag_solv(matrix, d)
