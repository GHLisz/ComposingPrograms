# http://composingprograms.com/pages/16-higher-order-functions.html


def trace(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return wrapped


@trace
def triple(x):
    return 3 * x

print(triple(12))

# equals to below


def triple(x):
    return 3 * x
triple = trace(triple)

