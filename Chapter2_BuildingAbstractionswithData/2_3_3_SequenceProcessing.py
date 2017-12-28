odds = [1, 3, 5, 7, 9]
print([x+1 for x in odds])
print([x for x in odds if 25 % x == 0])


def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

print(divisors(4))
print(divisors(12))

print([n for n in range(1, 1000) if sum(divisors(n)) == n])


def width(area, height):
    assert area % height == 0
    return area // height


def perimeter(width, height):
    return 2 * width + 2 * height


def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)

area = 80
print(width(area, 5))
print(perimeter(16, 5))
print(perimeter(10, 8))
print(minimum_perimeter(area))
print([minimum_perimeter(n) for n in range(1, 10)])


def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]


def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]


def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced


def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

print(divisors_of(12))

from operator import add


def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)


def perfect(n):
    return sum_of_divisors(n) == n

print(keep_if(perfect, range(1, 1000)))

apply_to_all = lambda map_fn, s: list(map(map_fn, s))
keep_if = lambda filter_fn, s: list(filter(filter_fn, s))

from functools import reduce
from operator import mul


def product(s):
    return reduce(mul, s)
