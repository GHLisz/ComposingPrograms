r = range(10000, 1000000000)


class LetterIter:
    """An iterator over letters of the alphabet in ASCII order."""
    def __init__(self, start='a', end='e'):
        self.next_letter = start
        self.end = end

    def __next__(self):
        if self.next_letter == self.end:
            raise StopIteration
        letter = self.next_letter
        self.next_letter = chr(ord(letter)+1)
        return letter

letter_iter = LetterIter()
print(letter_iter.__next__())
print(letter_iter.__next__())
print(next(letter_iter))
print(letter_iter.__next__())


class Positives:
    def __init__(self):
        self.next_positive = 1

    def __next__(self):
        result = self.next_positive
        self.next_positive += 1
        return result

p = Positives()
print(next(p))


class Letters:
    def __init__(self, start='a', end='e'):
        self.start = start
        self.end = end

    def __iter__(self):
        return LetterIter(self.start, self.end)

b_to_k = Letters('b', 'k')
first_iterator = b_to_k.__iter__()
print(next(first_iterator))
print(next(first_iterator))
second_iterator = iter(b_to_k)
print(second_iterator.__next__())
print(first_iterator.__next__())
print(first_iterator.__next__())
print(second_iterator.__next__())
print(second_iterator.__next__())


def double_and_print(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x

s = range(3, 7)
doubled = map(double_and_print, s)  # double_and_print not yet called
print(next(doubled))                       # double_and_print called once
print(next(doubled))                       # double_and_print called again
print(list(doubled))


def letters_generator():
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current)+1)

for letter in letters_generator():
    print(letter)

letters = letters_generator()
print(type(letters))
print(letters.__next__())


def all_pairs(s):
    for item1 in s:
        for item2 in s:
            yield (item1, item2)
print(list(all_pairs([1, 2, 3])))


class Stream:
    """A lazily computed linked list."""
    class empty:
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()

    def __init__(self, first, compute_rest=lambda: empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

s = Stream(1, lambda: Stream(2+3, lambda: Stream(9)))
print(s.rest.first)


def integer_stream(first):
    def compute_rest():
        return integer_stream(first+1)
    return Stream(first, compute_rest)


def map_stream(fn, s):
    if s is Stream.empty:
        return s

    def compute_rest():
        return map_stream(fn, s.rest)
    return Stream(fn(s.first), compute_rest)


def filter_stream(fn, s):
    if s is Stream.empty:
        return s

    def compute_rest():
        return filter_stream(fn, s.rest)
    if fn(s.first):
        return Stream(s.first, compute_rest)
    else:
        return compute_rest()


def first_k_as_list(s, k):
    first_k = []
    while s is not Stream.empty and k > 0:
        first_k.append(s.first)
        s, k = s.rest, k-1
    return first_k


def primes(pos_stream):
    def not_divible(x):
        return x % pos_stream.first != 0

    def compute_rest():
        return primes(filter_stream(not_divible, pos_stream.rest))
    return Stream(pos_stream.first, compute_rest)

prime_numbers = primes(integer_stream(2))
print(first_k_as_list(prime_numbers, 7))
