import copy


def get_size():
    n = int(input('Введіть кількість рядків квадратної матриці '))
    return n


n = get_size()


def get_matrix():
    global n
    matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = float(input(('Введіть  елемент ' + str(i + 1) + ' рядка ' + str(j+1) + ' стовпця матриці ')))
    return matrix


def print_matrix(mat):
    global n
    for i in range(0,n):
        print(mat[i])

    print(' ')


def get_vector(type):
    global n
    b = [1 for i in range(n)]
    for i in range(0, n ):
        b[i] = float(input(('Введіть ' + str(i+1) + ' елемент вектора ' + type + ' ')))
    return b


def multiplication(a, b):
    global n
    result = [[0.0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def get_sum(u, l, vec1, vec2):
    value = 0
    for k in range(l, u):
        value += vec1[k] * vec2[k]
    return value


def factorisation(a):
    global n
    lower = [[0 for i in range(n)] for i in range(n)]
    upper = [[0 for i in range(n)] for i in range(n)]

    for i in range(0, n):
        lower[i][0] = copy.copy(a[i][0])

    for j in range(0, n):
        upper[0][j] = copy.copy(a[0][j])/lower[0][0]

    for j in range(1, n):
        for i in range(1, n):
            col = [upper[i][j] for i in range(n)]
            if i >= j:
                val = get_sum(j, 0, lower[i], col)
                lower[i][j] = (a[i][j] - val)
                if i == j:
                    upper[i][j] = 1
            else:
                val = get_sum(i, 0, lower[i], col)
                upper[i][j] = (a[i][j]-val)/lower[i][i]
    print('Нижня трикутна матриця:')
    print_matrix(lower)

    print('Верхня трикутна матриця:')
    print_matrix(upper)

    test = multiplication(lower,upper)
    print_matrix(test)

    return lower, upper


def get_result(a):
    global n, d

    lower, upper = factorisation(a)
    y = [0.0 for i in range(n)]
    x = [0.0 for i in range(n)]


    y[0] = d[0]/lower[0][0]
    for i in range(0, n):
        y[i] = (d[i] - get_sum(i,0,lower[i], y) - get_sum(n,i+1,lower[i],y) )/lower[i][i]
    x[n-1] = y[n-i]/upper[n-1][n-1]
    for i in range(n-1, -1,-1):
        x[i] = (y[i] - get_sum(i,0,upper[i], x) - get_sum(n,i+1,upper[i],x) )/upper[i][i]

    for i in range(n):
        print("X " + str(i+1) + ' = ' + str(x[i]))




a = get_matrix()
d = get_vector('значеннь')

print_matrix(a)

get_result(a)













