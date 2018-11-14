"""
generators are a way of automatic iterator implementation syntax-wise, they are build like functions enriched with the yield keyword when next is first called on a generator, it finds the first yield and returns whatever is being yielded. Every next next call moves to the next yield and returns the yielded value. When there are no more yields to move to, StopIteration is raised
"""

def big_powers(n):
    n = int(n)
    for i in range(n):
        yield i**i

a = big_powers(5)
try:
    while True:
        print(next(a))
except StopIteration:
    print("Stop!")

"""
we can iterate over a generator like any other iterable
"""

a = big_powers(5)
for i in a:
    print(i)

print(big_powers(5))

"""
we print the generator object, not the values it yields
"""

print(*big_powers(5))

"""
the * operator unpacks the values yielded by the generator
"""

print(type(big_powers))

"""
we can see that big_powers is still a function and only its returned value is a generator
"""
