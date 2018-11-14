"""
let's enrich the list comprehension syntax with conditionals:
[expr for item in iterable if condition]
"""

a = [i for i in range(10) if i % 2 == 0]
print(a)

"""
shall produce the same results as:
"""

a = []
for i in range(10):
    if i % 2 == 0:
        a.append(i)
print(a)

"""
you can use more than one if which shall translate to the conjunction of their conditions
"""

a = [i for i in range(30) if i % 2 == 0 if i % 3 == 0]
print(a)

"""
shall produce the same results as:
"""

a = []
for i in range(30):
    if i % 2 ==  0 and i % 3 == 0:
        a.append(i)
print(a)
