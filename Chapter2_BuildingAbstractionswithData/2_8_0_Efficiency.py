def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

print(fib(5))


def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

fib = count(fib)
print(fib(19))
print(fib.call_count)


def count_frames(f):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

fib = count_frames(fib)
fib(19)
print(fib.open_count)
print(fib.max_count)
print(fib(24))
print(fib.max_count)


def memo(f):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

counted_fib = count(fib)
fib = memo(counted_fib)
print(fib(19))
print(counted_fib.call_count)
print(fib(34))
print(counted_fib.call_count)

