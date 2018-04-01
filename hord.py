from math import sin


def f(x):
    y = ((x - 3) ** 3) + (4 * sin(x))

    return y


def sdf(x):
    y = 6*(x-3) - 4*sin(x)

    return y


def initialization():
    a = float(input('Введіть значення а  '))
    b = float(input('Введіть значення б  '))

    return [a, b]


arr = initialization()
a = arr[0]
b = arr[1]
eps = 0.00001

if f(a)*f(b) < 0:
    if f(a) > f(b):
        x_prev = b
        x_curr = a
    elif f(a) < f(b):
        x_prev = a
        x_curr = b
else:
    b = b/2
    if f(a) * f(b) < 0:
        if f(a) > f(b):
            x_prev = b
            x_curr = a
        elif f(a) < f(b):
            x_prev = a
            x_curr = b

x_next = b
while abs(x_curr - x_prev) >= eps:

    x_next = x_curr - (x_prev-x_curr)*f(x_curr)/(f(x_prev) - f(x_curr))
    x_prev = x_curr
    x_curr = x_next
print('x = ', round(x_next, 4))
