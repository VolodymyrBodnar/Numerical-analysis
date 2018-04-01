import copy

matrix = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]

def get_matrix():
    global matrix
    for i in range(0, 3):
        for j in range(0, 3):
            matrix[i][j] = float(input(('Введіть  елемент ' + str(i +1)+' рядка '+str(j+1)+ ' стовпця матриці')))

    for k in range(0,3):
        matrix[k][3] = float(input('Введіть вектор значень'))


def if_singular():
    global matrix
    m1 = matrix[0][0]*matrix[1][1]*matrix[2][2]
    m2 = matrix[0][1]*matrix[1][2]*matrix[2][0]
    m3 = matrix[0][2]*matrix[1][0]*matrix[2][1]
    m4 = matrix[0][2]*matrix[1][1]*matrix[2][0]
    m5 = matrix[0][0]*matrix[1][2]*matrix[2][1]
    m6 = matrix[0][1]*matrix[1][0]*matrix[2][2]
    det = m1 +m2 +m3 -m4 -m5 -m6
    if det == 0:
        print("Матриця вироджена, система не має однозначного розв'язку")
        quit()


def output(matrix):
    out = copy.deepcopy(matrix)
    for i in range(0,3):
        for j in range (0, 3):
            out[i][j] = round(out[i][j],3)
    for i in range(0, 3):
        print(matrix[i])


def switch_rows(i, j):
    global matrix
    row_i = copy.deepcopy(matrix[i])
    row_j = copy.deepcopy(matrix[j])
    matrix[j] = row_i
    matrix[i] = row_j


def add_rows(row1, row2):
    row1_m = copy.deepcopy(row1)
    row2_m = copy.deepcopy(row2)
    for k in range(0, 4):
        row1_m[k] += row2_m[k]
    return row1_m


def row_times(row,x):

    row_m = copy.deepcopy(row)
    for k in range(0,4):
        row_m[k] *= x

    return row_m


def if_echelon():
    global matrix
    if matrix[1][0] == matrix[2][0] == matrix[2][1] == 0:
        return True
    return False


def max_in_col(j):
    global matrix
    main_in_col = matrix[j][j]
    main_row = j
    for i in range(j, 3):
        if abs(matrix[i][j]) >= abs(main_in_col):
            main_in_col = matrix[i][j]
            main_row = i
    return [main_in_col, main_row]


def gauss():
    global matrix
    echelon = False
    while not echelon:
        echelon = if_echelon()
        for j in range(0, 2):

            main = max_in_col(j)
            main_element = main[0]
            main_row = main[1]
            switch_rows(main_row, j)

            for i in range(j, 3):
                if matrix[i][j] != 0 and matrix[i][j] != main_element:
                    coef = -(matrix[i][j] / main_element)
                    main_row_modified = row_times(matrix[main_row], coef)
                    matrix[i] = add_rows(matrix[i], main_row_modified)
                    echelon = if_echelon()


def get_results():
    global matrix
    z = matrix[2][3]/matrix[2][2]
    y = (matrix[1][3] - matrix[1][2]*z)/matrix[1][1]
    x = (matrix[0][3] - matrix[0][1]*y - matrix[0][2]*z)/matrix[0][0]
    print('x = ', round(x,3))
    print('y = ', round(y,3))
    print('z = ', round(z,3))




get_matrix()
output(matrix)
if_singular()
gauss()
print('')
get_results()
