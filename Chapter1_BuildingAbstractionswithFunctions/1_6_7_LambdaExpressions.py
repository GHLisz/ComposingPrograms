# http://composingprograms.com/pages/16-higher-order-functions.html


def compose1(f, g):
    return lambda x: f(g(x))

s = lambda x: x * x
print(s)
print(s(12))

# compose2 behaves the same as compose1
compose2 = lambda f, g: lambda x: f(g(x))
