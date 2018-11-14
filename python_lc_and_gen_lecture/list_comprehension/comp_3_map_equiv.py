"""
the function map(func, iterable) returns a map, the i-th element of which is equal to func(i-th element of iterable passed as argument)
"""

a = list(map(lambda x : x **2, range(10)))
print(a)

"""
the same result can be achieved using list comprehension
"""

a = [i**2 for i in range(10)]
print(a)

"""
according to the documentation, the above statements are very close in terms of what code is executed
"""
