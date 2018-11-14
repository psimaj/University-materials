"""
list comprehension allows creating lists in a very tidy and clean manner

the basic syntax of a list comprehension is:
[expr for item in iterable]
where expr is an expression that might be dependent on item
"""

a = [i for i in range(10)]
print(a)

"""
the result of such expression is equivalent to:
"""

a = []
for i in range(10):
    a.append(i)
print(a)

"""
list comprehension provides a simple way of transforming lists
"""

a = [i**2 for i in a]
print(a)
