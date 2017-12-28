# http://composingprograms.com/pages/16-higher-order-functions.html


def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def cube(x):
    return x*x*x


def sum_cubes(n):
    return summation(n, cube)

result = sum_cubes(3)
print(result)
